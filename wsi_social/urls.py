from django.urls import path, re_path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt import views as jwt_views
from wsi_social.views import (usuario_view, front_view)

urlpatterns = [
    #swagger
    path('swagger-file/', SpectacularAPIView.as_view(), name='schema'),
    # redoc
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # swagger
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    #usuario
    path('api/usuario/', usuario_view.UsuarioViewSet.as_view(), name='usuario'),
    #login
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #index
    # re_path(r'', front_view.index, name='index'),
]
