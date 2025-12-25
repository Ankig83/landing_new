from django.shortcuts import render


def home(request):
    """Главная страница лендинга"""
    return render(request, 'pages/home.html')


def figma_hero(request):
    """Preview: только hero-блок из макета (для верстки/проверки)."""
    return render(request, 'pages/figma_hero.html')
