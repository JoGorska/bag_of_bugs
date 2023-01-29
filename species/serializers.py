from rest_framework import serializers
from .models import Species


class SpeciesSerializer(serializers.ModelSerializer):
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # size = serializers.PrimaryKeyRelatedField(queryset=Size.objects.all())
    # enviroment = serializers.PrimaryKeyRelatedField(queryset=Enviroment.objects.all())
    # stock_level = serializers.Field()
    class Meta:
        model = Species
        fields = (
            'id',
            'name',
            'slug',
            # 'stock_level'
            'latin_name',
            'description',
            'dangerous_species',
            'category',
            'size',
            'enviroment',
        )
