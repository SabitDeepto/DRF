from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from Manage_Merchant.models import CreateMerchant
from Manage_Merchant.serializers import CreateMerchantSerializer


class CreateMerchantViewSet(viewsets.ModelViewSet):
    queryset = CreateMerchant.objects.all()
    serializer_class = CreateMerchantSerializer
    permission_classes = (IsAuthenticated,)
