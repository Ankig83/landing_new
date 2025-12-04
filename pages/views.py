from django.shortcuts import render


def home(request):
    """Главная страница лендинга"""
    return render(request, 'pages/home.html')
