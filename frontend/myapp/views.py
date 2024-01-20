from django.shortcuts import render, HttpResponse
from .models import *
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from django.views.generic import TemplateView
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