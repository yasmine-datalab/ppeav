from rest_framework import viewsets
import rest_framework.permissions
from rest_framework.response import Response
from .models import structure
from .serializer import structureSerializer

class structureViewSet(viewsets.ModelViewSet):
    """
    
    """
    serializer_class = structureSerializer
    queryset = structure.objects.all()
    model= structure
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['create', 'update', 'destroy'] :
            permission_classes = [rest_framework.permissions.IsAdminUser]
        else:
            permission_classes = [rest_framework.permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    
   