from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .serializer import RegisterSerializer, ChangePasswordSerializer

from .permission import IsOwner


#Register API
class RegisterApi(generics.GenericAPIView):
    """
    register view
    """
    serializer_class = RegisterSerializer
    permission_classes = [IsAdminUser, ]
    def post(self, request):
        """
          save user
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": RegisterSerializer(user, context=self.get_serializer_context()).data,
            "message": "Utilisateur crée avec succès.",
        })


class DeleteAccount(generics.GenericAPIView):
    """
      delete account
    """
    serializer_class= RegisterSerializer
    model = User
    permission_classes = [IsAdminUser, ]

    def delete(self, request):
        """
        delete user
        """
        user = get_object_or_404(User,id = request.GET.get("id"))
        user.delete()
        return Response({"result":"user delete"})
  
class SetPassword(generics.GenericAPIView):
    """
    set password
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [IsAdminUser, IsOwner,]
    
    def post(self, request):
        """
            set password post method
        """
        self.object = self.request.user
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]})
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors)