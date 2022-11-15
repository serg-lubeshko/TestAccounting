from django.contrib import admin
from django.contrib.auth import login
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="test",
        default_version='v1',
        description="test_accounting",

    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/v1/accounting/', include('accounting.urls'), name='accounting'),
    path('rest/v1/users/', include('users.urls'), name='accounting'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('accounts/', include('rest_framework.urls')),

]
