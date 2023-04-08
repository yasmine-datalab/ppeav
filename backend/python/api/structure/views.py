"""  view """
from rest_framework import viewsets
import rest_framework.permissions
from .models import Structure
from .serializer import StructureSerializer

class StructureViewSet(viewsets.ModelViewSet):
    """
     view set
    """
    serializer_class = StructureSerializer
    queryset = Structure.objects.all()
    model= Structure

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['create', 'update', 'destroy'] :
            permission_classes = [rest_framework.permissions.IsAdminUser]
        else:
            permission_classes = [rest_framework.permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
