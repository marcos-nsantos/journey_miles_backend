from rest_framework import viewsets

from apps.statement.models import Statement
from apps.statement.serializer.statement_serializer import StatementSerializer


class StatementViewSet(viewsets.ModelViewSet):
    serializer_class = StatementSerializer
    queryset = Statement.objects.all()
