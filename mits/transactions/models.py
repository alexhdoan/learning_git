from __future__ import unicode_literals
from django.db import models

from entities.models import Group, Employee
from inventory_types.models import FixedItem, LifespanItem, Consumable, License
from locations.models import Location
from generic_types.models import LocationType, ConsumableGeneric

class GroupIssueFixed(models.Model):
	issuee = models.ForeignKey(Group)
	fixed_item = models.OneToOneField(FixedItem)
	issue_date = models.DateField('date issued')
	notes = models.CharField(max_length=120)
	class Meta:
		verbose_name_plural = "Issue (Group, Fixed)"
	def __str__(self):
		return self.issuee.name

class GroupIssueLifespan(models.Model):
	issuee = models.ForeignKey(Group)
	lifespan_item = models.OneToOneField(LifespanItem)
	issue_date = models.DateField('date issued')
	due_date = models.DateField('due date')
	notes = models.CharField(max_length=120)
	class Meta:
		verbose_name_plural = "Issue (Group, Lifespan)"
	def __str__(self):
		return self.issuee.name

class GroupCheckOutLifespan(models.Model):
	issuee = models.OneToOneField(Group)
	lifespan_item = models.ForeignKey(LifespanItem)
	issue_date = models.DateField('date issued')
	due_date = models.DateField('due date')
	notes = models.CharField(max_length=120)
	class Meta:
		verbose_name_plural = "Check-out (Group, Lifespan)"
	def __str__(self):
		return self.issuee.name

class EmployeeIssueFixed(models.Model):
	issuee = models.ForeignKey(Employee)
	fixed_item = models.OneToOneField(FixedItem)
	issue_date = models.DateField('date issued')
	notes = models.CharField(max_length=120)
	class Meta:
		verbose_name_plural = "Issue (Employee, Fixed)"
	def __str__(self):
		name = self.issuee.first_name + ' ' + self.issuee.last_name
		return name

class EmployeeIssueLifespan(models.Model):
	issuee = models.ForeignKey(Employee)
	lifespan_item = models.OneToOneField(LifespanItem)
	issue_date = models.DateField('date issued')
	notes = models.CharField(max_length=120)
	class Meta:
		verbose_name_plural = "Issue (Employee, Lifespan)"
	def __str__(self):
		name = self.issuee.first_name + ' ' + self.issuee.last_name
		return name

class EmployeeCheckOutLifespan(models.Model):
	issuee = models.ForeignKey(Employee)
	fixed_item = models.OneToOneField(FixedItem)
	issue_date = models.DateField('date issued')
	due_date = models.DateField('due date')
	notes = models.CharField(max_length=120)
	class Meta:
		verbose_name_plural = "Check-out (Employee, Lifespan)"
	def __str__(self):
		name = self.issuee.first_name + ' ' + self.issuee.last_name
		return name

class LicenseIssue(models.Model):
	issuee = models.ForeignKey(Employee)
	software = models.OneToOneField(License)
	issue_date = models.DateField('date issued')
	notes = models.CharField(max_length = 120)
	class Meta:
		verbose_name_plural = "Software Licenses"
	def __str__(self):
		name = self.issuee.first_name + ' ' + self.issuee.last_name
		return name

class ConsumableRequest(models.Model):
	requestor = models.ForeignKey(Employee)
	requested_item = models.ForeignKey(ConsumableGeneric)
	location = models.ForeignKey(Location)
	request_date = models.DateField('date requested')
	REQUEST_STATUS = (
	   ('R', 'Requested'),
	   ('O', 'Ordered'),
	   ('D', 'Deployed'),
	)
	status = models.CharField(max_length=1,
	choices = REQUEST_STATUS,
	default = 'R')
	notes = models.CharField(max_length = 120)
	class Meta:
		verbose_name_plural = "Consumable Requests"
	def __str__(self):
		return self.location.name

class CateringRequest(models.Model):
	requestor = models.ForeignKey(Employee)
	vendor = models.CharField(max_length = 20)
	head_count = models.IntegerField(default=1)
	location = models.ForeignKey(Location)
	request_date = models.DateField('date requested')
	delivery_date = models.DateTimeField('delivery date and time')
	REQUEST_STATUS = (
	   ('R', 'Requested'),
	   ('O', 'Ordered'),
	   ('D', 'Delivered'),
	)
	status = models.CharField(max_length=1,
	choices = REQUEST_STATUS,
	default = 'R')
	notes = models.CharField(max_length = 120)
	class Meta:
		verbose_name_plural = "Catering Requests"
	def __str__(self):
		return self.requested_item.name

