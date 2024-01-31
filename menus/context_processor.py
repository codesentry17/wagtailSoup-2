from .models import NavTab, Navbar
from parler.utils.context import switch_language


def get_nav_tab(request):
    current_language = request.LANGUAGE_CODE
    
    if current_language == 'en':
        if Navbar.objects.exists():
            navbar = Navbar.objects.first()
            return {
                'WebName1':navbar.name1,
                'WebName2':navbar.name2,
                'tabs':navbar.nav_tab.all()    
            }
        else:
            return {
                'WebName1':"Navbar",
                'WebName2':"Deleted",
                'tabs':None
            }
        
    elif current_language == 'mr':
        if Navbar.objects.exists():
            navbar = Navbar.objects.get(id=2)
            return {
                'WebName1':navbar.name1,
                'WebName2':navbar.name2,
                'tabs':navbar.nav_tab.all()    
            }
        else:
            return {
                'WebName1':"Navbar",
                'WebName2':"Deleted",
                'tabs':None
            }



    # name = Navbar.objects.first()
    # if NavTab.objects.exists():
    #     tabs = NavTab.objects.all()
    #     return {
    #         'WebName1':name.name1,
    #         'WebName2':name.name2,
    #         'tabs':tabs
    #     }



"""
{% if tabs %}

{% for tab in tabs %}

{% if tab.page_list.count() < 2 %}
    single page link

    name:nav_title
    url:tab.page_list.first().page_link.slug
{% else %}
    dropdown

    name:nav_title
    for page in tab.page_list.all():
        name:page.page_link.title
        url:page.page_link.slug
{% endif %}


{% endfor %}


{% endif %}

"""
