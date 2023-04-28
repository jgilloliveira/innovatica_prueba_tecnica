from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Modelo de usuario, es el modelo de django pero con la propiedad is_approved"""

    is_approved = models.BooleanField(default=False)
