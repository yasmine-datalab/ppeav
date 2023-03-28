from rest_framework import generics
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer

#Register API
class RegisterApi(generics.GenericAPIView):
    """
    register view
    """
    serializer_class = RegisterSerializer
    def post(self, request):
        """
          save user
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "Utilisateur crée avec succès.",
        })
