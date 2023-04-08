from django.urls import path, include
from rest_framework import routers

from .views import EnfantViewSet

router = routers.DefaultRouter()
router.register(r'', EnfantViewSet) # newly registered ViewSet

urlpatterns = [
    path('', include(router.urls)),
]
