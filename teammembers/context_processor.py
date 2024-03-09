from .models import Team
from wagtail.models import Locale

def get_team_cards(request):

    try:
        team = Team.objects.filter(locale=Locale.get_active())
    except Team.DoesNotExist:
        return {  }

    return {
        'team':team
    }

        

