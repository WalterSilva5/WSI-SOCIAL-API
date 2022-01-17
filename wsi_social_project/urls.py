from django.urls import path, include

urlpatterns = [
    path('', include('wsi_social.urls')),
]