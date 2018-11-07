from rest_framework import serializers
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from Manage_Call_Center.models import CreateExecutive


@permission_classes((IsAuthenticated,))
class CreateExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateExecutive
        fields = ('executive_name', 'email', 'phone')
