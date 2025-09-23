from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('base/', views.base, name='base'),
    path('chat_page/', views.chat_page, name='chat_page'),
    path('login_page/', views.login_page, name='login_page'),
    path("logout/", views.logout_page, name="logout"),
    path('signup_page/', views.signup_page, name='signup_page'),
]
