from django.urls import path
from . import views

#This is how you make pages:
urlpatterns = [
    path('', views.index, name='index'),#Root URL
    path('home/', views.home, name='home'),#Home page
    path('about/', views.about, name='about'),#About page
    path('contact/', views.contact, name='contact'),#Contact page
]
#Note these are all connected by the syntax home/ etc and the def  on what to do in the pages are in view.py which is where we have made all the func
