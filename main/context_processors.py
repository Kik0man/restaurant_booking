from .models import SiteContent

def background_image(request):
    path = request.path
    key_map = {
        '/': 'background_home',
        '/about/': 'background_about',
        '/booking/': 'background_booking',
        '/accounts/profile/': 'background_profile',
    }
    key = key_map.get(path, 'background_image')  # общий запасной
    bg = SiteContent.objects.filter(key=key).first()
    return {
        'background_image_url': bg.image.url if bg and bg.image else None
    }