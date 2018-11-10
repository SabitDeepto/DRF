from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from Hub.models import HubManager
from Hub.serializers import HubManagerSerializer


class HubManagerViewSet(viewsets.ModelViewSet):
    queryset = HubManager.objects.all()
    serializer_class = HubManagerSerializer