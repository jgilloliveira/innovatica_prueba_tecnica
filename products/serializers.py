from rest_framework import serializers
from products.models import Product, ProductPicture, ProductCategory


class ProductPictureSerializer(serializers.ModelSerializer):
    """Serializador de imágenes de productos"""

    class Meta:
        model = ProductPicture
        fields = ('id', 'picture',)


class ProductCategorySerializer(serializers.ModelSerializer):
    """Serializador de categorías de productos"""

    class Meta:
        model = ProductCategory
        fields = '__all__'


class RegisteredProductSerializer(serializers.ModelSerializer):
    """Serializador de productos para usuarios registrados, se muestra la primera imagen"""

    state_name = serializers.ReadOnlyField(read_only=True)
    categories = ProductCategorySerializer(many=True, required=False)
    first_picture = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_first_picture(self, obj):
        picture = obj.pictures.first()
        serializer = ProductPictureSerializer(picture)
        return serializer.data


class RegisteredDetailProductSerializer(serializers.ModelSerializer):
    """Serializador de detalle productos para usuarios registrados,
    se muestra todas las imágenes"""

    state_name = serializers.ReadOnlyField(read_only=True)
    categories = ProductCategorySerializer(many=True, required=False)
    pictures = ProductPictureSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Serializador de productos para usuarios no registrados"""

    state_name = serializers.CharField(read_only=True)

    class Meta:
        model = Product
        exclude = ('categories',)
