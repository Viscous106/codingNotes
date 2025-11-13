from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#you have to add all these files in frontEnd folder that you have to create in main dProject folder and connect the folder with settings.py
def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')





def index1(request):
    return HttpResponse('<h1>Yeah bitch first django site</h1>')
def home1(request):
    return HttpResponse('<h1>Home Page</h1>')
def about1(request):
    return HttpResponse('<h1>About Page</h1>')
def contact1(request):
    return HttpResponse('<h1>Contact Page</h1>')
