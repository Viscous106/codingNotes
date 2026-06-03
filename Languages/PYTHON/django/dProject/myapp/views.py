from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#you have to add all these files in frontEnd folder that you have to create in main dProject folder and connect the folder with settings.py
def index(request):
    dictionary={
        'name': 'Viscous',
        'age': 18
    }
    return render(request, 'index.html', dictionary)
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def counter(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
    else:
        name = request.GET.get('name', '')
        age = request.GET.get('age', '')

    content = {
        'name': name,
        'age': age
    }
    return render(request, 'counter.html', content)



def index1(request):
    return HttpResponse('<h1>Yeah bitch first django site</h1>')
def home1(request):
    return HttpResponse('<h1>Home Page</h1>')
def about1(request):
    return HttpResponse('<h1>About Page</h1>')
def contact1(request):
    return HttpResponse('<h1>Contact Page</h1>')
