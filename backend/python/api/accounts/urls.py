from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views import RegisterApi, deleteAccount, set_password


urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterApi.as_view(), name="sign_up"),
    path('api/deleteuser/', deleteAccount.as_view(), name="delete_account"),
    path('api/change-password/', set_password.as_view(), name='change-password'),
]
