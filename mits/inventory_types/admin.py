from django.contrib import admin

from .models import Consumable, FixedItem, LifespanItem, License 


admin.site.register(Consumable)
admin.site.register(FixedItem)
admin.site.register(LifespanItem)
admin.site.register(License)
