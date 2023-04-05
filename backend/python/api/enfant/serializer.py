from rest_framework import serializers
from .models import enfant

class enfantBulkCreateUpdateSerializer(serializers.ListSerializer):  
    """
    serializer for bulk create
    """
    def create(self, validated_data):  
        """
        create
        """
        data = [enfant(**item) for item in validated_data]  
        return enfant.objects.bulk_create(data)  
      

class enfantSerializer(serializers.ModelSerializer):
    """
        class enfant serializer
    """
    class Meta:
        """
            Meta class
        """
        model = enfant
        fields = '__all__'
        list_serializer_class = enfantBulkCreateUpdateSerializer

    