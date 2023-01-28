from rest_framework import generics
from .models import Species
from .serializers import SpeciesSerializer


class BugsList(generics.ListCreateAPIView):
    pass


class BugDetail(generics.RetrieveDestroyAPIView):
    pass
