from rest_framework import generics
from ihas.models import IHA
from ihas.serializers import IHASerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class IHAListCreateView(generics.ListCreateAPIView):
    """
    View to list and create IHA objects.

    Supports filtering and searching based on specific fields.
    """

    serializer_class = IHASerializer
    queryset = IHA.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["brand", "category", "weight", "model"]
    search_fields = ["brand", "category", "weight", "model"]


class IHARetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete an IHA object.
    """

    serializer_class = IHASerializer
    queryset = IHA.objects.all()
