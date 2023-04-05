from rest_framework import serializers
from .models import structure





class structureBulkCreateUpdateSerializer(serializers.ListSerializer):  
        """
         serializer for bulk create
        """
        def create(self, validated_data):  
            """
            create
            """
            data = [structure(**item) for item in validated_data]  
            return structure.objects.bulk_create(data) 
        


class structureSerializer(serializers.ModelSerializer):
    """
        class enfant serializer
    """
    class Meta:
        """
            Meta class
        """
        model = structure
        fields = '__all__'
        list_serializer_class = structureBulkCreateUpdateSerializer
    

    