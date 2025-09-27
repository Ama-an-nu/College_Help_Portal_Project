from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('base/', views.base, name='base'),
    path('chat_page/', views.chat_page, name='chat_page'),
    path('login_page/', views.login_page, name='login_page'),
    path("logout/", views.logout_page, name="logout"),
    path('signup_page/', views.signup_page, name='signup_page'),
    path("about/", views.about_page, name="about_page"),
    path("services/", views.services_page, name="services_page"),
    path("features/", views.features_page, name="features_page"),
    path("chatbot/", views.chatbot_page, name="chatbot_page"),
    path("notes_page/", views.notes_page, name="notes_page"),

]
