from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import json
from django.conf import settings
from django.http import HttpResponse
import os
from django.contrib.auth import login as django_login
from user_app.models import User
from urllib.parse import parse_qs
import hashlib
import hmac
from django.contrib.sessions.backends.db import SessionStore

# Create your views here.   

def serve_js(request):
    js_path = os.path.join(settings.BASE_DIR, f'staticfiles/main/js/telegram_bot.js')
    js_template_path = os.path.join(settings.BASE_DIR, js_path)
    with open(js_template_path, "r") as f:
        js_content = f.read()
    
    js_content = js_content.replace("{{ BACKEND_URL }}", settings.WEB_APP_URL)

    return HttpResponse(js_content, content_type="application/javascript")

@csrf_exempt
def create_session(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            parsed_query_auth_data = parse_qs(data.get('auth_data', ''))
            auth_data = {key: value[0] if len(value) == 1 else value for key, value in parsed_query_auth_data.items()}
            user_data = json.loads(auth_data['user'])
            received_hash = data.get('received_hash', '')
            data_check_string = data.get("data_check_string", "")


            if not data_check_string:
                return JsonResponse({
                    'status': 'error', 
                    'message': 'Missing dataCheckString!', 
                    'redirect_url': reverse('error'), 
                    'code': 400
                }, status=400)
            
            secret_key = hmac.new(
                 key="WebAppData".encode(),
                 msg=settings.BOT_TOKEN.encode(),
                 digestmod=hashlib.sha256
            ).digest()
            computed_hash = hmac.new(
                key=secret_key,       
                msg=data_check_string.encode(),  
                digestmod=hashlib.sha256
            ).hexdigest()

            result = computed_hash == received_hash   

            if not result:
                return JsonResponse({
                    'status': 'error', 
                    'message': 'Invalid authentication', 
                    'redirect_url': reverse('error'), 
                    'code': 403
                }, status=403)

            telegram_id = user_data.get('id')
            username = user_data.get('username', f'user_{telegram_id}')
            first_name = user_data.get('first_name', None)
            last_name = user_data.get('last_name', None)
    
            user, created = User.objects.get_or_create(
                username=username, 
                telegram_id=telegram_id,
                first_name=first_name, 
                last_name=last_name,
                is_active=True
            )

            user.backend = 'django.contrib.auth.backends.ModelBackend'
            django_login(request, user)

            request.session['_auth_user_id'] = str(user.id)
            request.session['_auth_user_backend'] = 'django.contrib.auth.backends.ModelBackend'
            request.session.save()

            return JsonResponse({
                'status': 'success', 
                'message': 'Authentication successful!', 
                'redirect_url': reverse('home_page'), 
                'code': 200
            }, status=200)
        
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e),
                'redirect_url': reverse('error'),
                'code': 500
            }, status=500)

    return JsonResponse({
        'status': 'error', 
        'message': 'Invalid request method', 
        'redirect_url': reverse('error'), 
        'code': 405
    }, status=405)

@csrf_exempt
def get_session_data(request, session_key=None):
    if not session_key: session_key = request.COOKIES.get('sessionid', None)
    session_data = SessionStore(session_key=session_key if session_key else request.session.session_key)

    return session_data