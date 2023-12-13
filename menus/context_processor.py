from .models import NavTab

def get_nav_tab(request):
    if NavTab.objects.exists():
        tabs = NavTab.objects.all()
        return {
            'tabs':tabs
        }
    
    return {'tabs':None}



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
