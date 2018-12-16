
from django.urls import path

from Manage_Ambassador import views

urlpatterns = [
    path('', views.create_ambassador, name='create_ambassador'),
    path('add', views.ambassador_list, name='add'),
    path('lists', views.amb_list, name='lists'),


]
