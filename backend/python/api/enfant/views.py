from rest_framework import viewsets
import rest_framework.permissions
from .models import Enfant
from .serializer import EnfantSerializer

class EnfantViewSet(viewsets.ModelViewSet):
    """
    
    """
    serializer_class = EnfantSerializer
    queryset = Enfant.objects.all()
    model= Enfant

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'create', 'update', 'destroy'] :
            permission_classes = [rest_framework.permissions.IsAdminUser]
        else:
            permission_classes = [rest_framework.permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
