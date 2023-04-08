from rest_framework import serializers
from .models import Structure





class StructureBulkCreateUpdateSerializer(serializers.ListSerializer):
    """
    serializer for bulk create
    """
    def create(self, validated_data):
        """
        create
        """
        data = [Structure(**item) for item in validated_data]
        return Structure.objects.bulk_create(data)

class StructureSerializer(serializers.ModelSerializer):
    """
        class enfant serializer
    """
    class Meta:
        """
            Meta class
        """
        model = Structure
        fields = '__all__'
        list_serializer_class = StructureBulkCreateUpdateSerializer
    