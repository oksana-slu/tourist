from django.conf import settings


def site_url(request):
    """
    Adds site-url from settings

    """
    return {'SITE_URL': settings.SITE_URL}
