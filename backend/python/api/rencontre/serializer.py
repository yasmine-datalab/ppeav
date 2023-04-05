from rest_framework import serializers
from .models import rencontre




class rencontreBulkCreateUpdateSerializer(serializers.ListSerializer):  
        """
         serializer for bulk create
        """
        def create(self, validated_data):  
            """
            create
            """
            data = [rencontre(**item) for item in validated_data]  
            return rencontre.objects.bulk_create(data)  
        


class rencontreSerializer(serializers.ModelSerializer):
    """
        class enfant serializer
    """
    class Meta:
        """
            Meta class
        """
        model = rencontre
        fields = '__all__'
        list_serializer_class = rencontreBulkCreateUpdateSerializer

    