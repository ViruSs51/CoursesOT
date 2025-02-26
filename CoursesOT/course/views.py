from django.shortcuts import render
from main.utils import load_svg

# Create your views here.
def course(request):
    data = {
        'icons': load_svg(),
    }
    
    return render(request, 'course/course_page.html', data)