from .models import Ad

def get_ads(request):
    
    try:
        ads = Ad.objects.all()
    except Ad.DoesNotExist:
        return { }
    
    return {
        'ads':ads
    }