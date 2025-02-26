import os
from pathlib import Path
from .models import Tag
from api.views import get_session_data
from user_app.models import User
from course.models import Course

def load_svg() -> dict:
    BASE_DIR = Path(__file__).parent.parent
    data = {}

    icon_dir = os.path.join(BASE_DIR, f'staticfiles/main/img/icon/')
    if os.path.exists(icon_dir):
        icon_files_name = [f for f in os.listdir(icon_dir) if os.path.isfile(os.path.join(icon_dir, f))]
        for f in icon_files_name:
            if f.endswith(".svg"):
                with open(os.path.join(icon_dir, f), 'r', encoding='utf-8') as icon:
                    data['_'.join(f.split('.svg')[0].split('-'))] = icon.read()

    return data

def get_tags():
    tags = Tag.objects.all()

    return tags.order_by('-usage_count')

def load_tags_on_request(request):
    tags = request.GET.get('tag', [])

    if tags:
        tags_list = tags.split('-+|+-')
        new_tags = []

        for tag in tags_list:
            if tags_list.count(tag) > 1:
                continue
            
            new_tags.append(tag)

        tags = new_tags

    
    return tags

def get_courses_user_paid(request):
    session_data = get_session_data(request)
    users = User.objects.filter(id=session_data.get('_auth_user_id'))
    courses_paid = []
    
    if users:
        for user in users:
            courses_paid = [course_paid.id for course_paid in user.course_paid.all()]
    
    return courses_paid