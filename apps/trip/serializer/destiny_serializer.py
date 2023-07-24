from rest_framework import serializers

from apps.trip.models.destiny_model import Destiny


class DestinySerializer(serializers.ModelSerializer):
    class Meta:
        model = Destiny
        fields = '__all__'
