from .models import Navbar
from wagtail.models import Locale

def get_nav_tab(request):

    try:
        navbar = Navbar.objects.filter(locale=Locale.get_active()).first()
        """the first() is required because the navbar data is only represented as a row and you've to retrieve that"""
    except Navbar.DoesNotExist:
        return {  }

    return {
        'WebName1':"Heart",
        'WebName2':navbar.name2,
        'WebNameOnClick':navbar.redirect,
        'tabs':navbar.nav_tab.all()
    }

        

