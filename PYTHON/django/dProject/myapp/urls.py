from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),#Root URL
    path('home/', views.home, name='home'),#Home page
    path('about/', views.about, name='about'),#About page
    path('contact/', views.contact, name='contact'),#Contact page
]
