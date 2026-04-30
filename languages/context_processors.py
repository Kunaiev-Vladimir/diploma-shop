from .models import Language


def active_languages(request):
    languages = Language.objects.filter(is_active=True)

    return {
        'active_languages': languages
    }