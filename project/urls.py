from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers

from apps.trip.views.destiny_view_set import DestinyViewSet
from apps.trip.views.statement_home_list_view import StatementHomeListView
from apps.trip.views.statement_view_set import StatementViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Journal Miles API",
        default_version='v1',
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register(r'statement', StatementViewSet)
router.register(r'destiny', DestinyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    path('statement-list-home/', StatementHomeListView.as_view(), name='statement-list-home'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
