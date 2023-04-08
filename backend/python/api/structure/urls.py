from django.urls import path, include
from rest_framework import routers

from .views import StructureViewSet

router = routers.DefaultRouter()
router.register(r'', StructureViewSet) # newly registered ViewSet

urlpatterns = [
    path('', include(router.urls)),
]
