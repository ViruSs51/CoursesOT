from django.shortcuts import render
from .utils import load_svg, get_tags

# Create your views here.

def home_page(request):
    data = {
        'icons': load_svg(),
        'tags': get_tags()
    }

    return render(request, 'main/home_page.html', data)
