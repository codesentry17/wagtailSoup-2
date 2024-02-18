from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail import blocks



from wagtail.contrib.forms.models import AbstractForm, AbstractFormField, FORM_FIELD_CHOICES
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel

from wagtail.contrib.forms.forms import FormBuilder
from wagtail.images.fields import WagtailImageField

import json
from os.path import splitext

from django.core.serializers.json import DjangoJSONEncoder

from wagtail.images import get_image_model



from wagtail.contrib.forms.views import SubmissionsListView
from django.utils.html import format_html
from django.urls import reverse

from wagtail.models import Collection


class CustomSubmissionsListView(SubmissionsListView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not self.is_export:
            # generate a list of field types, the first being the injected 'submission date'
            field_types = ['submission_date'] + [field.field_type for field in self.form_page.get_form_fields()]
            data_rows = context['data_rows']

            ImageModel = get_image_model()

            for data_row in data_rows:

                fields = data_row['fields']

                for idx, (value, field_type) in enumerate(zip(fields, field_types)):
                    if field_type == 'image' and value:
                        image = ImageModel.objects.get(pk=value)
                        rendition = image.get_rendition('fill-100x75|jpegquality-40')
                        preview_url = rendition.url
                        url = reverse('wagtailimages:edit', args=(image.id,))
                        # build up a link to the image, using the image title & id
                        fields[idx] = format_html(
                            "<a href='{}'><img alt='Uploaded image - {}' src='{}' />{}</a>",
                            url,
                            image.title,
                            preview_url,
                            image.title,
                        )

        return context



class FormField(AbstractFormField):

    field_type = models.CharField(
        verbose_name='field type',
        max_length=16,
        choices=list(FORM_FIELD_CHOICES) + [('image', 'Upload Image')]
    )

    page = ParentalKey('FormPage', related_name='form_fields', on_delete=models.CASCADE)



class CustomFormBuilder(FormBuilder):

    def create_image_field(self, field, options):
        return WagtailImageField(**options)




class FormPage(AbstractForm):

    form_builder = CustomFormBuilder

    submissions_list_view_class = CustomSubmissionsListView

    uploaded_image_collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    settings_panels = AbstractForm.settings_panels + [
        FieldPanel('uploaded_image_collection')
    ]

    def get_uploaded_image_collection(self):
        """
        Returns a Wagtail Collection, using this form's saved value if present,
        otherwise returns the 'Root' Collection.
        """
        collection = self.uploaded_image_collection
        return collection or Collection.get_first_root_node()   


    header = models.CharField()
    sub_header = models.CharField()

    extra_info = StreamField([
        ('Block',blocks.StructBlock([
            ('label', blocks.CharBlock()),
            ('description', blocks.CharBlock())
        ]))
    ],use_json_field=True, collapsed=True, blank=True)


    content_panels = AbstractForm.content_panels + [
        MultiFieldPanel([
            FieldPanel("header"),
            FieldPanel("sub_header"),
            FieldPanel("extra_info")
        ], heading="Non-Form Data"),
        InlinePanel("form_fields", label="Field")
    ]


    @staticmethod
    def get_image_title(filename):
        """
        Generates a usable title from the filename of an image upload.
        Note: The filename will be provided as a 'path/to/file.jpg'
        """

        if filename:
            result = splitext(filename)[0]
            result = result.replace('-', ' ').replace('_', ' ')
            return result.title()
        return ''

    def process_form_submission(self, form):
        """
        Processes the form submission, if an Image upload is found, pull out the
        files data, create an actual Wgtail Image and reference its ID only in the
        stored form response.
        """

        cleaned_data = form.cleaned_data

        for name, field in form.fields.items():
            if isinstance(field, WagtailImageField):
                image_file_data = cleaned_data[name]
                if image_file_data:
                    ImageModel = get_image_model()

                    kwargs = {
                        'file': cleaned_data[name],
                        'title': self.get_image_title(cleaned_data[name].name),
                        # 'collection': self.get_uploaded_image_collection(),
                    }

                    if form.user and not form.user.is_anonymous:
                        kwargs['uploaded_by_user'] = form.user

                    image = ImageModel(**kwargs)
                    image.save()
                    # saving the image id
                    # alternatively we can store a path to the image via image.get_rendition
                    cleaned_data.update({name: image.pk})
                else:
                    # remove the value from the data
                    del cleaned_data[name]

        return self.get_submission_class().objects.create(
            form_data=form.cleaned_data, 
            # cls=DjangoJSONEncoder, 
            # note: Wagtail 3.0 & beyond will no longer need to wrap this in json.dumps as it uses Django's JSONField under the hood now - https://docs.wagtail.org/en/stable/releases/3.0.html#replaced-form-data-textfield-with-jsonfield-in-abstractformsubmission
            page=self,
        )
























# class FormField(AbstractFormField):

#     page = ParentalKey("FormPage", related_name = 'form_fields', on_delete=models.CASCADE)





