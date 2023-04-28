from django.contrib import admin
from products.models import Product, ProductCategory, ProductPicture


class ProductPictureInline(admin.TabularInline):
    """Clase para mostrar la sección de imágenes en el admin de productos"""

    model = ProductPicture


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    """Admin de categorías de productos"""

    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin de productos"""

    list_display = ('id', 'name', 'state')
    filter_horizontal = ('categories',)
    inlines = [ProductPictureInline]
