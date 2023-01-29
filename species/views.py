from rest_framework import generics
from .models import Species
from .serializers import SpeciesSerializer


class BugsList(generics.ListCreateAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    depth = 1


class BugDetail(generics.RetrieveDestroyAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    lookup_field = 'slug'
