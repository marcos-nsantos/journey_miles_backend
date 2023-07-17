from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.apps.statement.views.statement_view_set import StatementViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Journal Miles API",
        default_version='v1',
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register(r'statement', StatementViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    # Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
