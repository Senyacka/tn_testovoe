from django.db import models
from azs.models import AZS


class Fuel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    fuel_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)


class AZSFuel(models.Model):
    azs = models.ForeignKey(AZS, on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
