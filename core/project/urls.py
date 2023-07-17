from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.apps.statement.views.statement_view_set import StatementViewSet

router = routers.DefaultRouter()
router.register(r'statement', StatementViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
