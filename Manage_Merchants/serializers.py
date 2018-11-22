from rest_framework import serializers

from Manage_Merchants.models import CreateMerchant


class CreateMerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateMerchant
        fields = ('id', 'merchant_name', 'email', 'phone')