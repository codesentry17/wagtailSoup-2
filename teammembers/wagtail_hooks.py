from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import Team

class TeamViewSet(SnippetViewSet):
    model = Team
    icon = 'user'
    list_display = ('full_name', 'designation', 'contact',)


register_snippet(TeamViewSet)