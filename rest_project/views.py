# from rest_framework import serializers
from django.shortcuts import render


def login(request):
    return render(request, 'auth_login.html')


def signup(request):
    return render(request, 'auth_register.html')


def index(request):
    return render(request, 'index.html')

