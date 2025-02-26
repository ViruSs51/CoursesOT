from django.urls import path
from . import views


urlpatterns = [
    path("serve-js/", views.serve_js, name="serve_js"),
    path('create-session/', views.create_session, name='create_session')
]
