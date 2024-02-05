from django.shortcuts import render

# Create your views here.
def advert_post(request):
    context = {}
    return render(request, 'pages/ad_post_page.html', context)