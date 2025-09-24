from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def dashboard(request):
    return render(request, 'core/dashboard.html')

def chat_page(request):
    return render(request, 'core/chatbot.html')

def base(request):
    return render(request, 'core/base.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome !! {user.first_name or user.username} 👋")
            return redirect("base")  
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'core/login.html')

def logout_page(request):
    logout(request)
    return redirect("login")

def signup_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "❌ Passwords do not match")
            return redirect("signup_page")

        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠️ Username already taken")
            return redirect("signup_page")

        if User.objects.filter(email=email).exists():
            messages.error(request, "⚠️ Email already registered")
            return redirect("signup_page")

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, f"🎉 Account created for {username}! Please log in.")
        return redirect("login_page")

    return render(request, "core/signup.html")
   

def about_page(request):
    return render(request, "core/about.html")


def services_page(request):
    return render(request, "core/services.html")


def features_page(request):
    return render(request, "core/features.html")
