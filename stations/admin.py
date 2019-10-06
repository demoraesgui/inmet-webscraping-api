from django.contrib import admin
from .models import MeteorologicalStation, MeteorologicalData
# Register your models here.

admin.site.register(MeteorologicalStation)
admin.site.register(MeteorologicalData)