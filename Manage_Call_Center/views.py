from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from Manage_Call_Center.models import CreateExecutive
from Manage_Call_Center.serializers import CreateExecutiveSerializer


class CreateExecutiveViewSet(viewsets.ModelViewSet):
    queryset = CreateExecutive.objects.all()
    serializer_class = CreateExecutiveSerializer
    permission_classes = (IsAuthenticated,)

