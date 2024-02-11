from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField

class FormField(AbstractFormField):

    page = ParentalKey("FormPage", related_name = 'form_fields', on_delete=models.CASCADE)


class FormPage(AbstractForm):

    header = models.CharField()
    sub_header = models.CharField()

    extra_info = StreamField([
        ('Block',blocks.StructBlock([
            ('label', blocks.CharBlock()),
            ('description', blocks.CharBlock())
        ]))
    ],use_json_field=True, collapsed=True, blank=True)


    content_panels = AbstractForm.content_panels + [
        FieldPanel("header"),
        FieldPanel("sub_header"),
        FieldPanel("extra_info"),
        InlinePanel("form_fields", label="Field")
    ]


# Create your models here.
