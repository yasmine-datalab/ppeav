import pandas as pd
from rest_framework import serializers
from enfant.serializer import enfantBulkCreateUpdateSerializer
from rencontre.serializer import rencontreBulkCreateUpdateSerializer
from structure.serializer import structureBulkCreateUpdateSerializer
from .models import CSVFile, RENCONTRE, STRUCTURE, CHILDREN

class CSVFileSerializer(serializers.ModelSerializer):
    """
        class enfant serializer
    """
    class Meta:
        """
            Meta class
        """
        model = CSVFile
        fields = '__all__'
    
    def create(self, validated_data):
        csv_file = validated_data["file"]
        type = validated_data["model"]
        data = pd.read_csv(csv_file).to_dict("records")
        if type == RENCONTRE:
            rencontres = rencontreBulkCreateUpdateSerializer(data)
            rencontres.is_valid(raise_exception=True)
            rencontres.save()
        elif type == CHILDREN:
            children = enfantBulkCreateUpdateSerializer(data)
            children.is_valid(raise_exception=True)
            children.save()
        elif type == STRUCTURE:
            structure = structureBulkCreateUpdateSerializer(data)
            structure.is_valid(raise_exception=True)
            structure.save()
        else: 
            raise serializers.ValidationError("Invalid file")
        return super().create(validated_data)