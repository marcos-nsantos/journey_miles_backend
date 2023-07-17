from rest_framework import viewsets

from core.apps.statement.models import Statement
from core.apps.statement.serializer.statement_serializer import StatementSerializer


class StatementViewSet(viewsets.ModelViewSet):
    serializer_class = StatementSerializer
    queryset = Statement.objects.all()
