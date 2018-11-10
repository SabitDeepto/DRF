from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from Manage_Merchant.models import CreateMerchant, PickUp
from Manage_Merchant.serializers import CreateMerchantSerializer, PickUpSerializer


class CreateMerchantViewSet(viewsets.ModelViewSet):
    queryset = CreateMerchant.objects.all()
    serializer_class = CreateMerchantSerializer


class PickUpViewSet(viewsets.ModelViewSet):
    queryset = PickUp.objects.all()
    serializer_class = PickUpSerializer