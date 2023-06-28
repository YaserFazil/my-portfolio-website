from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the payments index.")


