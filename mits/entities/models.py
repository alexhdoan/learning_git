from django.db import models
from django.contrib.auth.models import User
from generic_types.models import EntityType

class Entity(models.Model):
	id_number = models.CharField(max_length=30, verbose_name = "ID number")
	#entity_type = models.ForeignKey(EntityType, verbose_name = "type")
	class Meta:
		abstract = True


class Employee(Entity):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		my_name = self.first_name+' '+self.last_name
		return my_name	

class Group(Entity):
	name = models.CharField(max_length=60)
	contact = models.ForeignKey(Employee)
	def __str__(self):
		return self.name