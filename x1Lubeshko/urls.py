from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView

from users.views.jwt_login_view import MyTokenObtainPairView

# schema_view = get_schema_view(
#     openapi.Info(
#         title="test",
#         default_version='v1',
#         description="test_accounting",
#
#
#
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny, ],
# )

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

urlpatterns = [
    path('b-login/', MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
    path('rest/v1/accounting/', include('accounting.urls'), name='accounting'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    path('a-user/', include('users.urls')),

]
