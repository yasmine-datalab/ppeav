from rest_framework import serializers
from .models import Rencontre




class RencontreBulkCreateUpdateSerializer(serializers.ListSerializer):
    """
    serializer for bulk create
    """
    def create(self, validated_data):
        """
        create
        """
        data = [Rencontre(**item) for item in validated_data]
        return Rencontre.objects.bulk_create(data)



class RencontreSerializer(serializers.ModelSerializer):
    """
        class enfant serializer
    """
    class Meta:
        """
            Meta class
        """
        model = Rencontre
        fields = '__all__'
        list_serializer_class = RencontreBulkCreateUpdateSerializer
    