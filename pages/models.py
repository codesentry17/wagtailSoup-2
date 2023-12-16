from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


from streams import blocks as bk


# Create your models here.


class HomePage(Page):
    max_count = 1

    subtitle = models.CharField(max_length=50)

    content_panels = Page.content_panels + [FieldPanel("subtitle")]


class FlexPage(Page):
    body = models.TextField(blank=True, null=True)

    main_carousel = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("main_carousel"),
    ]




class Wiggle(Page):
    """practise the page models"""

    carousel = StreamField(
        [('carousel',bk.Carousel())],
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('carousel')
            ],
            heading = "Carousel",
        )
    ]
