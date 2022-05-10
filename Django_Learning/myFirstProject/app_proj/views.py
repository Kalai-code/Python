from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app_home(request):
    return HttpResponse("Welcome to Django app_proj Home Page")

