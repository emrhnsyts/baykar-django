from rest_framework import generics
from rents.permissions import IsObjectOwner
from rents.models import Rent
from rents.serializers import (
    RentCreateSerializer,
    RentListSerializer,
    RentRetrieveUpdateDestroySerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class RentListCreateView(generics.ListCreateAPIView):
    """
    View to list rent objects for the authenticated user.

    Supports filtering and searching based on specific fields.
    """

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
        "iha__model",
        "iha__category",
        "iha__weight",
        "iha__brand",
        "rent_start_date",
        "rent_end_date",
    ]
    search_fields = [
        "iha__model",
        "iha__category",
        "iha__weight",
        "iha__brand",
        "rent_start_date",
        "rent_end_date",
    ]

    def get_queryset(self):
        return Rent.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return RentCreateSerializer
        return RentListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a rent object.

    Restricted to the owner of the rent object.
    """

    serializer_class = RentRetrieveUpdateDestroySerializer
    queryset = Rent.objects.all()
    permission_classes = [IsObjectOwner]
