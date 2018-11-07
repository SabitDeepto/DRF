from rest_framework import viewsets

from Manage_Merchant.models import CreateMerchant
from Manage_Merchant.serializers import CreateMerchantSerializer


class CreateMerchantViewSet(viewsets.ModelViewSet):
    queryset = CreateMerchant.objects.all()
    serializer_class = CreateMerchantSerializer
