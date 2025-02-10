from django.shortcuts import render

from .utils import load_svg

# Create your views here.

def home_page(request):
    data = {
        'icons': load_svg()
    }

    return render(request, 'main/home_page.html', data)