from django.shortcuts import render
from user_app.models import User
from course.models import Course

# Create your views here.
def home_page(request):

    return render(request, 'main/home_page.html')