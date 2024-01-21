from django.shortcuts import render, HttpResponse
from .models import *
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from django.views.generic import TemplateView
from django.http import JsonResponse
from .tests import *
from scripts.test_openai import *
from src.web_scrape import *
import random

from src.main import generate_video
from src.captions import generate_captions_video

def execute_dummy(request):
  dropdown1_value = request.GET.get('dropdown1', '')

  result = generate_story(dropdown1_value)
  #generate_video(result, "./assets/SubwaySurfers.mov", "./static/videos/test_output.mov")
  return JsonResponse({'result': result})

def execute_video(request):
  results = request.GET.get('param1', '')
  dropdown2_value = request.GET.get('param2', '')
  generate_video(results, "./assets/SubwaySurfers.mov", "./static/videos/test_output.mov")
  return JsonResponse({'result': results})

def execute_real(request):
  dropdown1_value = request.GET.get('dropdown1', '')
  dropdown2_value = request.GET.get('dropdown2', '')

  urls = scrape(dropdown1_value)
  urls.pop(0)
  urls = list(set(urls))
  # Returns a list of strings (stories)
  result = scrape_story(urls)[random.randint(0, len(urls) - 1)]

  generate_video(result, "./assets/SubwaySurfers.mov", "./static/videos/test_output.mov")
  return JsonResponse({'result': result})

def execute_history(request):
  dropdown1_value = request.GET.get('dropdown1', '')
  dropdown2_value = request.GET.get('dropdown2', '')

  result = scrape_history(dropdown1_value)

  generate_video(result, "./assets/SubwaySurfers.mov", "./static/videos/test_output.mov")
  return JsonResponse({'result': result})

def execute_history_custom(request):
  dropdown1_value = request.GET.get('dropdown1', '')
  dropdown2_value = request.GET.get('dropdown2', '')

  result = scrape_history(dropdown1_value)

  generate_video(result, "./assets/SubwaySurfers.mov", "./static/videos/test_output.mov")
  return JsonResponse({'result': result})

# Create your views here.

def home(request):
  return render(request, "home.html")

def create(request):
    return render(request, "create.html")

# def options(request):
#     return render(request, "options.html")

def story_options(request):
    return render(request, "story_options.html")

def ai(request):
    return render(request, "ai.html")

def real_posts(request):
    return render(request, "real_posts.html")

def history(request):
    return render(request, "history.html")

def custom(request):
    return render(request, "custom.html")

def history_options(request):
    return render(request, "history_options.html")

def history_custom(request):
    return render(request, "history_custom.html")