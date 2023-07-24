from rest_framework import generics

from apps.trip.models.statement_model import Statement
from apps.trip.serializer.statement_serializer import StatementSerializer


class StatementHomeListView(generics.ListAPIView):
    queryset = Statement.objects.all()[0:3]
    serializer_class = StatementSerializer
