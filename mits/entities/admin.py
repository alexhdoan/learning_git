from django.contrib import admin

from .models import Group, Employee

admin.site.register(Employee)
admin.site.register(Group)
