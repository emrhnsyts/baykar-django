from django.db import models
from django.contrib.auth.models import User

# Choices for IHA models
ihas = (
    ("AKINCI", "Akinci"),
    ("DIHA", "Diha"),
    ("MINI IHA", "Mini IHA"),
    ("TB2", "TB2"),
    ("TB3", "TB2"),
)
# Choices for IHA weight categories
weights = (
    ("IHA 0", "IHA 0"),
    ("IHA 1", "IHA 1"),
    ("IHA 2", "IHA 2"),
    ("IHA 3", "IHA 3"),
)


class IHA(models.Model):
    """
    IHA model representing unmanned aerial vehicles.
    """
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30, choices=ihas)
    weight = models.CharField(max_length=10, choices=weights)
    category = models.CharField(max_length=50)
    rented_by = models.ManyToManyField(
        User, through="rents.Rent", through_fields=("iha", "user")
    )
