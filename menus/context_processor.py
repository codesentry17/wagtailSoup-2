from .models import Navbar
from wagtail.models import Locale

def get_nav_tab(request):

    navbar = Navbar.objects.get(locale=Locale.get_active())

    return {
        'WebName1':navbar.name1,
        'WebName2':navbar.name2,
        'tabs':navbar.nav_tab.all()
    }