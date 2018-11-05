from rest_framework import serializers


class SayHello(serializers.Serializer):
    name = serializers.CharField(required=False)
    dob = serializers.DateField(input_formats=['%Y-%m-%d'])

