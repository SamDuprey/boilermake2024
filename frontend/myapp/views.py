from django.shortcuts import render, HttpResponse
from .models import TodoItem
from .models import Project
from .models import MyForm
from .models import *
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from django.http import JsonResponse
from .tests import *
from scripts.test_openai import *

def execute_dummy(request):
    dropdown1_value = request.GET.get('dropdown1', '')
    dropdown2_value = request.GET.get('dropdown2', '')

    result = generate_story(dropdown1_value)
    return JsonResponse({'result': result})

# Create your views here.

def home(request):
    return render(request, "home.html")

def create(request):
    return render(request, "create.html")

def contact(request):
    return render(request, "contact.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def contentForm(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            dropdown_value = form.cleaned_data['dropdown_field']
            
            # Pass the value to your other Python script
            result = dropdown_value
            print(result)
            
            return render(request, 'result.html', {'result': result})
    else:
        form = MyForm()

    return render(request, 'create.html', {'form': form})

def dropdownsearch(request):
    if request.method=="POST":
        searchgender=request.POST.get('gender')
        searchdesignation=request.POST.get('designation')
        empsearch=Employee.objects.filter(gender=searchgender,designation=searchdesignation)
        return render(request,'home.html',{"data":empsearch})
    else:
        displayemp=Employee.objects.all()

        return render(request,'home.html',{"data":displayemp})
