# from rest_framework import serializers
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from rest_project.forms import RegisterForm


def home(request):
    count = User.objects.count()

    return render(request, 'index.html', {'count': count})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("./")
    else:
        form = RegisterForm()
    return render(request, 'template/register.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'registration/signup.html', {'form': form})


def hub(request):
    return render(request, 'forms_regular.html', {'name': 'Hub Registration'})


def hub_table(request):
    return render(request, 'tables_regular.html', {'name': 'Hub'})


def merchant(request):
    return render(request, 'tables_regular.html', {'name': 'Merchant'})


def pickup(request):
    return render(request, 'forms_regular.html', {'name': 'Pick Up Request'})


def call_centre_executive(request):
    return render(request, 'tables_regular.html', {'name': 'Call Centre Executive'})


def handle_pickup_request(request):
    return render(request, 'forms_regular.html', {'name': 'Call Centre Executive Registration'})


def fulfill_manager(request):
    return render(request, 'forms_regular.html', {'name': 'Fulfill Manager Registration '})


def check_order(request):
    return render(request, 'tables_regular.html', {'name': 'Orders'})

