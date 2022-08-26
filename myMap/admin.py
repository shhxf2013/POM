from django.contrib.gis import admin
from myMap.models import myMap

# Register your models here.
@admin.register(myMap)
class myMapAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'location')