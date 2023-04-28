from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from products.models import Product
from products.serializers import ProductSerializer, RegisteredProductSerializer, RegisteredDetailProductSerializer
from products.permissions import IsApprovedPermission


class ProductViewSet(viewsets.ModelViewSet):
    """Vista de productos"""

    queryset = Product.objects.all()
    permission_classes = [IsApprovedPermission]
    # Filtros por nombre, estado y categoría
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = {
        'name': ['icontains'],
        'state': ['exact'],
        'categories__name': ['exact']
    }

    def get_serializer_class(self):
        # Si esta sentencia es verdadera se trata de un AnonymousUser
        if self.request.user.pk is None:
            return ProductSerializer
        # Si la acción es retrieve entonces es por detalles de producto
        elif self.action == 'retrieve':
            return RegisteredDetailProductSerializer
        return RegisteredProductSerializer
