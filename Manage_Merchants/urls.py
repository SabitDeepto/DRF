from django.urls import path, include
from rest_framework import routers
# from rest_framework.routers import SimpleRouter

from . import views

router = routers.DefaultRouter()
router.register('merchant', views.CreateMerchantViewSet)

urlpatterns = [

        path('', include(router.urls))


]