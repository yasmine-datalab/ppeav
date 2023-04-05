# Create your views here.
import pandas as pd

from rest_framework.viewsets import generics
from rest_framework.response import Response
from .serializer import CSVFileSerializer
from .models import CSVFile
import rest_framework.permissions

# ViewSets define the view behavior.

class fileLoadViews(generics.ListCreateAPIView):
    """
        file load view
    """
    model = CSVFile
    serializer_class = CSVFileSerializer
    permission_classes = [rest_framework.permissions.IsAdminUser, ]
    def post(self, request):
        """
          save csv
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        csv = serializer.save()
        return Response({
            "user": CSVFileSerializer(csv, context=self.get_serializer_context()).data,
            "message": "Utilisateur crée avec succès.",
        })
    
