# from rest_framework import serializers
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def signup(request):
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def login(request):
    return render(request, 'registration/login.html')


