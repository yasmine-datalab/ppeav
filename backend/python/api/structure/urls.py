from django.urls import path, include
from rest_framework import routers

from .views import structureViewSet

router = routers.DefaultRouter()
router.register(r'', structureViewSet) # newly registered ViewSet

urlpatterns = [
    path('', include(router.urls)),
]