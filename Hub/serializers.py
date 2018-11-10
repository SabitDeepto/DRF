from rest_framework import serializers

from Hub.models import HubManager


class HubManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HubManager
        fields = ('id', 'url')