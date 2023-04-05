from django.urls import path, include
from rest_framework import routers

from .views import enfantViewSet

router = routers.DefaultRouter()
router.register(r'', enfantViewSet) # newly registered ViewSet

urlpatterns = [
    path('', include(router.urls)),
]