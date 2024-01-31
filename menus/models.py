# Create your models here.
from django.db import models
# Create your models here.

from wagtail.snippets.models import register_snippet
from wagtail.models import TranslatableMixin


from wagtail.admin.panels import FieldPanel, InlinePanel, PageChooserPanel, FieldRowPanel
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel



class PageList(Orderable):
    """table to hold navbar tab page dropdown"""
    
    nav_tab = ParentalKey('NavTab', related_name='page_list')
    
    page_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        related_name='+',
        on_delete=models.CASCADE
    )

    panels = [
        PageChooserPanel('page_link')
    ]


class NavTab(ClusterableModel, Orderable):
    """the navbar tabs"""

    navbar = ParentalKey('Navbar', related_name='nav_tab')

    nav_title = models.CharField(max_length=20, blank=True, null=True)

    panels = [
        FieldPanel('nav_title'),
        InlinePanel('page_list', label='Your Page/s')
    ]

    @property
    def is_dropdown(self):
        return self.page_list.count() > 1

    @property
    def routes(self):
        return {x.page_link.url for x in self.page_list.all()}
        

    def save(self, **kwargs):
        if not self.nav_title:
            self.nav_title = self.page_list.first().page_link.title
        super(NavTab,self).save(**kwargs)

    def __str__(self) -> str:
        return "NavTab"


@register_snippet
class Navbar(ClusterableModel, TranslatableMixin):
    """the navbar that holds NavTabs"""

    name1 = models.CharField(max_length=15)
    name2 = models.CharField(max_length=15)

    panels = [
        FieldRowPanel(
            [
                FieldPanel('name1'),
                FieldPanel('name2')
            ],
            heading="WebSite Name",
        ),
        InlinePanel('nav_tab', label='Nav Item/s')
    ]

    class Meta:
        unique_together = ('translation_key', 'locale')

    def __str__(self) -> str:
        return "Navbar"
    
