"""  Serializer """
from rest_framework import serializers
from .models import Enfant

class EnfantBulkCreateUpdateSerializer(serializers.ListSerializer):
    """
    serializer for bulk create
    """
    def create(self, validated_data):
        """
        create
        """
        data = [Enfant(**item) for item in validated_data]
        return Enfant.objects.bulk_create(data)

class EnfantSerializer(serializers.ModelSerializer):
    """
        class enfant serializer
    """
    class Meta:
        """
            Meta class
        """
        model = Enfant
        fields = '__all__'
        list_serializer_class = EnfantBulkCreateUpdateSerializer

    