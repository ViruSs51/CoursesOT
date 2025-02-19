from django.shortcuts import render
from .utils import load_svg, get_tags
from course.models import Course
from api.views import get_session_data

# Create your views here.
def error(request):
    if request.method == 'GET':
        data = {
            'message': request.GET.get('message'),
            'status': f'Error: {request.GET.get("status")}'
        }

        return render(request, 'main/error.html', data)

def home_page(request):
    courses = Course.objects.all()
    data = {
        'icons': load_svg(),
        'tags': get_tags(),
        'courses': courses,
        'courses_media': {f'{c.id}': c.media.all() for c in courses}
    }

    session_data = get_session_data(request)
    #print(session_data.get('_bot_name'), session_data.get('_auth_user_id'))
    #print(request.COOKIES.get('sessionid', None))

    return render(request, 'main/home_page.html', data)
