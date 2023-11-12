from django.urls import path
from . import views
from .views import index, profil

urlpatterns = [
    path('', index, name ='home'),
    path('about_me/', profil, name ='about_me'),
]
