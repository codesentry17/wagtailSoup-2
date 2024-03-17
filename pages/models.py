from django.db import models

from wagtail.models import Page, Orderable, Locale
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import StreamField, RichTextField
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail import blocks

from streams import blocks as bk
from streams import blocks2 as bk2

from teammembers.models import Team


# create your page models here


class Wiggle(Page):
    """supreme app for making pages"""

    components = StreamField(
        [
            ("banner_carousel", bk.BannerCarousel()),
            ("about_us", bk.AboutUs()),
            ("page_intro", blocks.BooleanBlock(default=True)),
            ("blog_section", bk.BlogSection()),
            ("team_section", bk.TeamSection()),
            ("fact_band", bk2.FactsBand()),

        ],
        use_json_field=True,
        collapsed=True,
    )

    content_panels = Page.content_panels + [FieldPanel("components")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        chosen_components = [field.block.name for field in self.components]

        if "blog_section" in chosen_components:
            context["child_blogs"] = self.get_children().type(Blog)
            """beauty of the above line is that it could only select get_children and go on. 
            But we tell it to specifically search for page models that have been built using the Blog class among the child pages."""


        if "team_section" in chosen_components:
            """Bringing the snippet context into the page if team_section component is selected by admin"""
            context["team"] = Team.objects.filter(locale=Locale.get_active())

        return context














class Blog(Page):
    """This is going to create blog pages"""

    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    short_description = models.CharField(blank=True)

    component = StreamField(
        [
            ("section", bk2.Section()),
            ("fact_band", bk2.FactsBand()),
        ],
        use_json_field=True,
        collapsed=True,
        blank=True,
    )

    blog_list_header = models.CharField(max_length=20, blank=True, null=True, default="Other Blogs")

    show_advertisement = models.BooleanField(default=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("header_image"), 
                        FieldPanel("short_description")
                    ],
                    heading="Blog Card Data",
                ),
                FieldPanel("component"),
            ],
            heading="Left Section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("blog_list_header"),
                FieldPanel('show_advertisement'),
            ],
            heading="Right Section"
        )
    ]
