from django.urls import path, include
from rest_framework import routers
# from rest_framework.routers import SimpleRouter

from . import views

router = routers.DefaultRouter()
router.register('types', views.TypeViewSet)
router.register('languages', views.LanguageViewSet)
router.register('programmers', views.ProgrammerViewSet)

urlpatterns = [

        path('', include(router.urls)),
        path('', include(router.urls)),
        path('', include(router.urls)),


]