from django.urls import path
from . import views

urlpatterns = [
    path('doctor/', views.doctor_chat, name='doctor_chat'),
    path('video/', views.video_consultation, name='video_consultation'),
    path('room/<str:room_name>/', views.chat_room, name='chat_room'),
]
