from django.urls import path, include
from . import views, utils


urlpatterns = [
    path(f'{id}/', views.course, name=f'course-{id}')
    for id in utils.load_courses_id()
]