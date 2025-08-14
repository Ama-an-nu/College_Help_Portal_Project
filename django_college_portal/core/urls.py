from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('base/', views.base, name='base'),
    path('chat_page/', views.chat_page, name='chat_page'),
]
