from django.db import models
from django.utils import timezone

# Create your models here.


# Criação da Model das Estações Meteorologicas
class MeteorologicalStation(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    altitude = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    state = models.CharField(max_length=2, null=False)
    city = models.CharField(max_length=30, null=False)

    created_date = models.DateTimeField(default=timezone.now)
    edited_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.state + ' - ' + self.city


# Dados da estação meteorológica
class MeteorologicalData(models.Model):
    MeteorologicalStation = models.ForeignKey(
        MeteorologicalStation, on_delete=models.DO_NOTHING, null=False, verbose_name="Estação Meteorológica")

    T_max = models.FloatField(null=True)
    T_min = models.FloatField(null=True)
    RH_max = models.FloatField(null=True)
    RH_min = models.FloatField(null=True)
    Rn = models.FloatField(null=True)
    U = models.FloatField(null=True)
    P = models.FloatField(null=True)
    Ri = models.FloatField(null=True)
    date = models.DateTimeField(null=False, default=timezone.now)

    created_date = models.DateTimeField(default=timezone.now)
    edited_date = models.DateTimeField(default=timezone.now)
