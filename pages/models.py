from django.db import models

from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import StreamField, RichTextField
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail import blocks

from streams import blocks as bk



# Create your models here.


class HomePage(Page):
    max_count = 1

    subtitle = models.CharField(max_length=50)

    content_panels = Page.content_panels + [FieldPanel("subtitle")]




class Wiggle(Page):

    """supreme app for making pages"""

    components = StreamField([
        ('banner_carousel', bk.BannerCarousel()),
        ('about_us', bk.AboutUs()),
        ('page_intro', blocks.BooleanBlock(default=True)),
        ('blog_section',bk.BlogSection())
        ], use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("components")
    ]

    subpage_types = ['Blog']




class Blog(Page):
    """This is going to create blog pages"""

    card_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    card_description = models.CharField(max_length=50, blank=True)






    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('card_image'),
                FieldPanel('card_description')
            ],
            heading="Blog Card Glimpse"
        ),

    ]


