from rest_framework import serializers
from .models import Species


class SpeciesSerializer(serializers.ModelSerializer):

    stock_level = serializers.ReadOnlyField()

    class Meta:
        model = Species
        fields = (
            'id',
            'slug',
            'name',
            'price',
            'stock_level',
            'latin_name',
            'description',
            'dangerous_species',
            'category',
            'size',
            'enviroment',
        )
