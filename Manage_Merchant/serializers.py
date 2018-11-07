from rest_framework import serializers


from Manage_Merchant.models import CreateMerchant


class CreateMerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateMerchant
        fields = ('merchant_name', 'email', 'phone')
