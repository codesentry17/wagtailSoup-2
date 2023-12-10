from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
# Create your models here.

class HomePage(Page):
    max_count = 1

    subtitle = models.CharField(max_length=50)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle')
    ]


class FlexPage(Page):

    body = models.TextField(blank=True, null=True)

    main_carousel = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('main_carousel'),
    ]