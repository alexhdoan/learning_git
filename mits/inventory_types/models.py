from __future__ import unicode_literals

from django.db import models

from generic_types.models import FixedGeneric, LifespanGeneric, EntityType, LocationType, ConsumableGeneric


class Consumable(models.Model):
    barcode = models.CharField(max_length=50)
    consumable_type = models.ForeignKey(ConsumableGeneric, verbose_name = "type")
    quantity = models.IntegerField(default=1)
    def __str__(self):
    	return self.consumable_type.name

class FixedItem(models.Model):
	STATUSES = (
		('I', 'in-use'),
		('A', 'available')
	)
	barcode = models.CharField(max_length=50)
	fixed_type = models.ForeignKey(FixedGeneric, verbose_name = "type")
	status = models.CharField(max_length = 1, choices = STATUSES, default = 'A')
	notes = models.CharField(max_length=120)
	def __str__(self):
		return self.fixed_type.name
	class Meta:
		verbose_name_plural = "Fixed Items"

class LifespanItem(models.Model):
	STATUSES = (
		('I', 'in-use'),
		('A', 'available'),
		('D', 'damaged'),
	)
	barcode = models.CharField(max_length=50)
	lifespan_type = models.ForeignKey(LifespanGeneric, verbose_name = "type")
	status = models.CharField(max_length = 1, choices = STATUSES, default = 'A')
	notes = models.CharField(max_length=120)
	def __str__(self):
		return self.lifespan_type.name
	class Meta:
		verbose_name_plural = "Lifespan Items"

class License(models.Model):
	software = models.CharField(max_length = 25)
	license_number = models.CharField(max_length=50)
	def __str__(self):
		return self.software