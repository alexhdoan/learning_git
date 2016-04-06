from __future__ import unicode_literals

from django.db import models

from django.contrib import admin

from generic_types.models import LocationType, ConsumableGeneric

from smart_selects.db_fields import ChainedManyToManyField

def get_default():
    return LocationType.objects.get(id=1)

class Location(models.Model):
    name = models.CharField(max_length=50)
    location_type = models.ForeignKey(LocationType, verbose_name = "type", default=1)
    #stocked = models.ManyToManyField(ConsumableGeneric, verbose_name="stocked at location")
    stocked = ChainedManyToManyField(
    	ConsumableGeneric,
    	chained_field="location_type",
    	chained_model_field="stocked_in",
    	)
    def __str__(self):
    	return self.name
