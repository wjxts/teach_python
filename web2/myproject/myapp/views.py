# myapp/views.py
from django.shortcuts import render
from .models import Person

def dynamic_page(request, name):
    print(name)
    person = Person(name=name)
    #person = Person.objects.get(name=name)
    return render(request, 'index.html', {'person': person})
    #return render(request, 'index.html')