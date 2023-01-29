from rest_framework import generics
from .models import Species
from .serializers import SpeciesSerializer


class BugsList(generics.ListCreateAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    pass


class BugDetail(generics.RetrieveDestroyAPIView):
    pass
