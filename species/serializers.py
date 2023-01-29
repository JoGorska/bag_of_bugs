from rest_framework import serializers
from .models import Species, Category, Size, Enviroment


class SpeciesSerializer(serializers.ModelSerializer):
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # size = serializers.PrimaryKeyRelatedField(queryset=Size.objects.all())
    # enviroment = serializers.PrimaryKeyRelatedField(queryset=Enviroment.objects.all())

    class Meta:
        model = Species
        fields = (
            'id',
            'name',
            'slug',
            'latin_name',
            'description',
            'dangerous_species',
            'category',
            'size',
            'enviroment',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class EnviromentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enviroment
        fields = '__all__'