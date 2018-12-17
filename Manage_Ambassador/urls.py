
from django.urls import path

from Manage_Ambassador import views

urlpatterns = [
    path('', views.create_ambassador, name='create_ambassador'),
    path('list', views.ambassador_list, name='ambassador_list'),
    path('delete_ambassador', views.delete_ambassador, name='delete_ambassador'),



]
