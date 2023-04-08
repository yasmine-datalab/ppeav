import pandas as pd
from rest_framework import serializers
from enfant.serializer import EnfantSerializer
from rencontre.serializer import  RencontreSerializer
from structure.serializer import  StructureSerializer
from .models import CSVFiles, RENCONTRE, STRUCTURE, CHILDREN

class CSVFileSerializer(serializers.ModelSerializer):
    """
        class enfant serializer
    """
    class Meta:
        """
            Meta class
        """
        model = CSVFiles
        fields = '__all__'
    
    def create(self, validated_data):
        """
            create
        """
        csv_file = validated_data["file"]
        typ = validated_data["model"]
        
        if typ == RENCONTRE:
            cle = "codecoupon"
            data = pd.read_csv(csv_file, sep=";")
            data = data.drop_duplicates(cle, keep="first").to_dict("records")
            rencontres = RencontreSerializer(data=data, many=True)
            rencontres.is_valid(raise_exception=True)
            rencontres.save()
        elif typ == CHILDREN:
            cle = "matricule"
            data = pd.read_csv(csv_file, sep=";")
            data = data.drop_duplicates(cle, keep="first").to_dict("records")
            children = EnfantSerializer(data=data, many=True)
            children.is_valid(raise_exception=True)
            children.save()
        elif typ == STRUCTURE:
            cle = "structure"
            data = pd.read_csv(csv_file, sep=";")
            data = data.drop_duplicates(cle, keep="first").to_dict("records")
            structure = StructureSerializer(data=data, many=True)
            structure.is_valid(raise_exception=True)
            structure.save()
        else:
            raise serializers.ValidationError("Invalid file")
        return super().create(validated_data)