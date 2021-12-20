from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from main_app import settings

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)
# Create your views here.
@cache_page(CACHE_TTL)
def home(request):
    print("view is executed")
    return render(request, "index.html")
