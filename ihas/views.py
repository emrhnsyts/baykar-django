from rest_framework import generics
from ihas.models import IHA
from ihas.serializers import IHASerializer
from rents.serializers import RentSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
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


class IHARentView(generics.CreateAPIView):
    """
    View to create a rent object for a specific IHA.
    """
    serializer_class = RentSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a rent object associated with the specified IHA.
        """
        pk = kwargs.get("pk")
        iha = get_object_or_404(IHA, pk=pk)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, iha=iha)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
