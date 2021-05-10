from django.urls import path, include
from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularRedocView,
                                   SpectacularSwaggerView)


urlpatterns = [
    path('api/', include([
        path('auth/', include('authentication.urls')),
        path('features/', include('features.urls')),

    ])),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(
        url_name='schema'), name='swagger-ui'),
    path('redoc', SpectacularRedocView.as_view(
        url_name='schema'), name='redoc'),
]
