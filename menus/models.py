# Create your models here.
from django.db import models
# Create your models here.

from wagtail.snippets.models import register_snippet


from wagtail.admin.panels import FieldPanel, InlinePanel, PageChooserPanel
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


class NavTab(ClusterableModel):
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
        return {x.page_link.url for x in self.page_list.all() }
        

    def save(self, **kwargs):
        if not self.nav_title:
            self.nav_title = self.page_list.first().page_link.title
        super(NavTab,self).save(**kwargs)


@register_snippet
class Navbar(ClusterableModel):
    """the navbar that holds NavTabs"""

    panels = [
        InlinePanel('nav_tab', label='Nav Item/s')
    ]


    def __str__(self) -> str:
        return "Navbar"