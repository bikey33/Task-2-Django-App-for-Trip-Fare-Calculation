from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name = 'home'), # Route urls with 'fareapp/home/' to home viewfunction

]