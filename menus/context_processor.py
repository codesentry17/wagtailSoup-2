from .models import Navbar
from wagtail.models import Locale

def get_nav_tab(request):

    try:
        navbar = Navbar.objects.filter(locale=Locale.get_active()).first()
        return {
            'WebName1':navbar.name1,
            'WebName2':navbar.name2,
            'tabs':navbar.nav_tab.all()
        }
    except Navbar.DoesNotExist:
        return {  }


        

