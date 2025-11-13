# How To Make a django project:
Step1:install django in the local machin by "pip install django"
Step2: django-admin startproject Project-name

## How to make a app instide the project :
> python manage.py startapp appname

## how to run DJANGO setup:
> python manage.py runserver

## How to make frontend or add frontend to the project:

```
First of all make a dir in the main folder then connect the directory to the settings.py Templates section now add the fortend portion in templates and then connect them via views.py and urls.py
```

## How to store html inputed data using get:
```
make a url in urls.py where you can make a get endoint
connect  it to a normal function and add the variable via html method get
```
```
def counter(request):
    name = request.GET['name']  # 'text' is the name attribute of the input field in your HTML form
    age = request.GET['age']
    content = {
        'name': name,
        'age': age
    }
    return render(request, 'counter.html',content)
```