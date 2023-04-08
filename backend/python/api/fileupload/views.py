# Create your views here.
from rest_framework.viewsets import generics
import rest_framework.permissions

from .serializer import CSVFileSerializer
from .models import CSVFiles

# ViewSets define the view behavior.

class fileLoadViews(generics.ListCreateAPIView):
    """
        file load view
    """
    model = CSVFiles
    serializer_class = CSVFileSerializer
    permission_classes = [rest_framework.permissions.IsAdminUser, ]
