from rest_framework import serializers
from django.contrib.auth.models import User

# Register serializer


class RegisterSerializer(serializers.ModelSerializer):
    """
     register serializer
    """
    class Meta:
        """
            Meta class
        """
        model = User
        fields = ('id', 'username', 'password', 'first_name',
                  'last_name', 'is_superuser', 'is_staff')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        password=validated_data['password'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        is_superuser=validated_data['is_superuser'],
                                        is_staff=validated_data["is_staff"])
        return user

# User serializer


# class UserSerializer(serializers.ModelSerializer):
#     """
#         user
#     """
#     class Meta:
#         """
#             meta
#         """
#         model = User
#         fields = '__all__'

class ChangePasswordSerializer(serializers.Serializer):
    """
        change pwd serializer
    """
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
