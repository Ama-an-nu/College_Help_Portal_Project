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
            return redirect("base")  # change to your homepage/dashboard
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'core/login.html')

def logout_page(request):
    logout(request)
    return redirect("login")

def signup_page(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("signup_page")

        if User.objects.filter(username=email).exists():
            messages.error(request, "User already exists")
            return redirect("signup_page")

        user = User.objects.create_user(username=email, email=email, password=password1)
        user.first_name = full_name
        user.save()

        messages.success(request, "Account created! Please log in.")
        return redirect("login_page")
    return render(request, 'core/signup.html')

