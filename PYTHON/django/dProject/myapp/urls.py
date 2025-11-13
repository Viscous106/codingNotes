from django.urls import path
from . import views

#This is how you make pages:
urlpatterns = [
    #html via render:
    path('',views.index, name='index'),#Root URL
    path('home/', views.home, name='home'),#Home page
    path('about/', views.about, name='about'),#About page
    path('contact/', views.contact, name='contact'),#Contact page
    
    #html via https:
    path('index1/', views.index1, name='index1'),#index1 URL
    path('home1/', views.home1, name='home1'),#Home1 page
    path('about1/', views.about1, name='about1'),#About1 page
    path('contact1/', views.contact1, name='contact1'),#Contact1 page\
        
    #to take input from html form:
    path('counter', views.counter, name='counter')
]
#Note these are all connected by the syntax home/ etc and the def  on what to do in the pages are in view.py which is where we have made all the func
