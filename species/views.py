from rest_framework import generics
from .models import Species, Category, Size, Enviroment
from .serializers import (
    SpeciesSerializer, CategorySerializer, SizeSerializer, EnviromentSerializer
)


class BugsList(generics.ListCreateAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    depth = 1
    pass


class BugDetail(generics.RetrieveDestroyAPIView):
    pass


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    depth = 1
    pass


class SizeList(generics.ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    depth = 1
    pass


class EnviromentList(generics.ListCreateAPIView):
    queryset = Enviroment.objects.all()
    serializer_class = EnviromentSerializer
    depth = 1
    pass