from django.urls import path, include
from rest_framework import routers

from .views import rencontreViewSet

router = routers.DefaultRouter()
router.register(r'', rencontreViewSet) # newly registered ViewSet

urlpatterns = [
    path('', include(router.urls)),
]