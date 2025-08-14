from django.shortcuts import render

def dashboard(request):
    return render(request, 'core/dashboard.html')

def chat_page(request):
    return render(request, 'core/chatbot.html')

def base(request):
    return render(request, 'core/base.html')