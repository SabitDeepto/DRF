from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api_test.models import Paradigm, Programmer, Language
from api_test.serializers import ParadigmSerializer, LanguageSerializer, ProgrammerSerializer


class ParadigmViewSet(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
