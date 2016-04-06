from __future__ import unicode_literals
from django.db import models

class FixedGeneric(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return str(self.name)
	

class LifespanGeneric(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return str(self.name)

class EntityType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
    	return self.name

class LocationType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
    	return self.name

class ConsumableGeneric(models.Model):
    name = models.CharField(max_length=30)
    stocked_in = models.ManyToManyField(LocationType)
    def __str__(self):
        return str(self.name)
