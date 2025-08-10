from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('chat/', views.chat_page, name='chat_page'),
]
