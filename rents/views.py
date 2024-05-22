from rest_framework import generics
from rents.permissions import IsObjectOwner
from rents.models import Rent
from rents.serializers import RentListSerializer, RentRetrieveUpdateDestroySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class RentListView(generics.ListAPIView):
    """
    View to list rent objects for the authenticated user.
    
    Supports filtering and searching based on specific fields.
    """
    serializer_class = RentListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["iha__model","iha__category","iha__weight","iha__brand","rent_start_date", "rent_end_date"]
    search_fields = ["iha__model","iha__category","iha__weight","iha__brand","rent_start_date", "rent_end_date"]

    def get(self, request, *args, **kwargs):
        """
        List rent objects for the authenticated user.
        """
        self.queryset = Rent.objects.filter(user=request.user)
        return self.list(request, *args, **kwargs)


class RentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a rent object.

    Restricted to the owner of the rent object.
    """
    serializer_class = RentRetrieveUpdateDestroySerializer
    queryset = Rent.objects.all()
    permission_classes = [IsObjectOwner]
