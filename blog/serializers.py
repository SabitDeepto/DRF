from rest_framework import serializers


class SayHelloSerializer(serializers.Serializers):
    name = serializers.CharField(required=False)
    dob = serializers.DateField(input_formats=['%Y-%m-%d'], required=False)

