from django.urls import path, include
from rest_framework import routers

from .views import RencontreViewSet

router = routers.DefaultRouter()
router.register(r'', RencontreViewSet) # newly registered ViewSet

urlpatterns = [
    path('', include(router.urls)),
]
