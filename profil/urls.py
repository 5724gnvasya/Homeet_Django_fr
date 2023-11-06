from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name ='home'),
]
urlpattern1 = [
    path('', views.AboutPageView.as_view(), name ='profil'),
]