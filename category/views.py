from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from category.models import Product
from category.serializers import ProductSerializers


class ProductViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for CRUD operations on the Product model.
    """
    queryset = Product.objects.all()  # Retrieve all Product objects
    serializer_class = ProductSerializers

    def create(self, request, *args, **kwargs):
        """
        Override the create method to handle custom logic, if necessary.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Validate the data
        self.perform_create(serializer)  # Save the validated data
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        """
        Save the object to the database.
        """
        serializer.save()

    def list(self, request, *args, **kwargs):
        """
        Override the list method to fetch all products.
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Fetch a single product by ID.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        Handle full updates for a product.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a product by ID.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_update(self, serializer):
        """
        Save updates to the database.
        """
        serializer.save()

    def perform_destroy(self, instance):
        """
        Remove the object from the database.
        """
        instance.delete()
