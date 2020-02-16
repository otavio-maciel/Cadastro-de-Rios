from django.contrib import admin
from .models import River, Sensor, Reading


admin.site.register(River)
admin.site.register(Sensor)
admin.site.register(Reading)
