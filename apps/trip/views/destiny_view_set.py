from rest_framework import viewsets, filters, status
from rest_framework.response import Response

from apps.trip.models.destiny_model import Destiny
from apps.trip.serializer.destiny_serializer import DestinySerializer


class DestinyViewSet(viewsets.ModelViewSet):
    serializer_class = DestinySerializer
    queryset = Destiny.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response({"message": "no destiny was found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
