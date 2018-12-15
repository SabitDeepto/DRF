
from django.urls import path, include

from Manage_Ambassador import views

urlpatterns = [
    path('/', views.create_ambassador, name='create_ambassador'),


]
