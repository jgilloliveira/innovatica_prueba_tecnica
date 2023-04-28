from django.db import models


class ProductCategory(models.Model):
    """Modelo de categorías de productos"""

    name = models.CharField(max_length=100)


class Product(models.Model):
    """Modelo de productos"""

    IN_STOCK = 'D'
    SOLD_OUT = 'A'
    STATUS_CHOICES = [(IN_STOCK, 'Disponible'), (SOLD_OUT, 'Agotado')]
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=STATUS_CHOICES)
    categories = models.ManyToManyField(
        ProductCategory,
        related_name='products',
        blank=True
    )

    @property
    def state_name(self):
        return dict(self.STATUS_CHOICES).get(self.state)


class ProductPicture(models.Model):
    """Modelo de imágenes de productos"""

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='pictures')
    picture = models.FileField(blank=True, null=True)
