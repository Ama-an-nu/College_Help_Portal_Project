from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('base/', views.base, name='base'),

    path('login_page/', views.login_page, name='login_page'),
    path("logout/", views.logout_page, name="logout"),
    path('signup_page/', views.signup_page, name='signup_page'),
    path("about/", views.about_page, name="about_page"),
    path("services/", views.services_page, name="services_page"),
    path("features/", views.features_page, name="features_page"),
    path("chatbot/", views.chatbot_page, name="chatbot_page"),
    path("notes_page/", views.notes_page, name="notes_page"),
    path("landing/", views.landing_page, name="landing"),
    path('login_page/', auth_views.LoginView.as_view(template_name='login.html'), name='login_page'),
    path("logout/", LogoutView.as_view(next_page="login_page"), name="logout"),
    path("chatbot/", views.chatbot_page, name="chatbot_page"),

]
