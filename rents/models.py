from django.db import models
from django.contrib.auth.models import User

from ihas.models import IHA


class Rent(models.Model):
    """
    Rent model representing the rental of an IHA.
    """
    iha = models.ForeignKey(IHA, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rent_start_date = models.DateTimeField()
    rent_end_date = models.DateTimeField()
