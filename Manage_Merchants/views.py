from rest_framework import viewsets

from Manage_Merchants.models import CreateMerchant
from Manage_Merchants.serializers import CreateMerchantSerializer


class CreateMerchantViewSet(viewsets.ModelViewSet):
    queryset = CreateMerchant.objects.all()
    serializer_class = CreateMerchantSerializer