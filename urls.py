from django.urls import path
from . import views

urlpatterns = [
    path('templates/video_generator/', views.generate_video, name='generate_video'),
]
