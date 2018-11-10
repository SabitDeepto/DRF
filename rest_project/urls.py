"""rest_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from Hub.views import HubManagerViewSet
from Manage_Call_Center.views import CreateExecutiveViewSet
from Manage_Merchant.views import CreateMerchantViewSet, PickUpViewSet
from api_test.views import ParadigmViewSet, ProgrammerViewSet, LanguageViewSet

router = SimpleRouter()
router.register('center', CreateExecutiveViewSet, base_name='CreateExecutive')
router.register('merchant', CreateMerchantViewSet, base_name='CreateMerchant')

router.register('paradigm', ParadigmViewSet,)
router.register('programmer', ProgrammerViewSet, )
router.register('language', LanguageViewSet,)

router.register('pick_my_product', PickUpViewSet,)
router.register('pickup_request', HubManagerViewSet,)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(router.urls)),

    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),

    path('', include(router.urls)),
    path('', include(router.urls)),




]
