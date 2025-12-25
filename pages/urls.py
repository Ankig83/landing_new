from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('figma-hero/', views.figma_hero, name='figma_hero'),
]

