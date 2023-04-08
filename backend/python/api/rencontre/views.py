from rest_framework import viewsets
import rest_framework.permissions
from .models import Rencontre
from .serializer import RencontreSerializer

class RencontreViewSet(viewsets.ModelViewSet):
    """
        rencontre
    """
    serializer_class = RencontreSerializer
    queryset = Rencontre.objects.all()
    model= Rencontre

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['create', 'update', 'destroy'] :
            permission_classes = [rest_framework.permissions.IsAdminUser]
        else:
            permission_classes = [rest_framework.permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
