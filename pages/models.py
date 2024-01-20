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
    """practise the page models"""

    components = StreamField([
        ('banner_carousel', bk.BannerCarousel()),
        ('about_us', bk.AboutUs()),
        ('page_intro', blocks.BooleanBlock(default=False)),
        ], use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("components")
    ]



    # # old one >>>    

    # carousel = StreamField(
    #     [('carousel',bk.Carousel())],
    #     use_json_field=True,
    # )

    # content_panels = Page.content_panels + [
    #     MultiFieldPanel(
    #         [
    #             FieldPanel('carousel')
    #         ],
    #         heading = "Carousel",
    #     )
    # ]








class BlogPage(Page):

    # Database fields

    body = RichTextField()
    date = models.DateField("Post date")
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    # Search index configuration

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date'),
    ]


    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body'),
        InlinePanel('related_links', heading="Related links", label="Related link"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        FieldPanel('feed_image'),
    ]




class BlogPageRelatedLink(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='related_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]