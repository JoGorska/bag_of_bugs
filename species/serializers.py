from rest_framework import serializers
from .models import Species


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = (
            'id',
            'name',
            'slug',
            'latin_name',
            'description',
            'dangerous_species',
            'category__name',
            'size__name',
            'enviroment__name',

        )
