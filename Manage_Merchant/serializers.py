from rest_framework import serializers


from Manage_Merchant.models import CreateMerchant, PickUp


class CreateMerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateMerchant
        fields = ('merchant_name', 'email', 'phone')


class PickUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickUp
        fields = ('id', 'address', 'product_details', 'product_quantity', 'contact_number', )