from rest_framework import viewsets

from apps.trip.models.destiny_model import Destiny
from apps.trip.serializer.destiny_serializer import DestinySerializer


class DestinyViewSet(viewsets.ModelViewSet):
    serializer_class = DestinySerializer
    queryset = Destiny.objects.all()
