import json
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect

# Create your views here.
def auth(request):
    request.session.flush()

    if request.method == 'GET':
        bot_name = request.GET.get('bot_name')
        request.session['_bot_name'] = bot_name
        request.session.save()

    return render(request, 'user_app/auth.html')

def logout(request):
    request.session.flush()
    django_logout(request)

    return redirect('home_page')