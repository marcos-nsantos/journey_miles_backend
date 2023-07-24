from rest_framework import viewsets

from apps.trip.models import Statement
from apps.trip.serializer.statement_serializer import StatementSerializer


class StatementViewSet(viewsets.ModelViewSet):
    serializer_class = StatementSerializer
    queryset = Statement.objects.all()
