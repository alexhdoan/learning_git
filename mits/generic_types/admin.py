from django.contrib import admin

from .models import FixedGeneric, LifespanGeneric, EntityType, LocationType, ConsumableGeneric

admin.site.register(ConsumableGeneric)
admin.site.register(FixedGeneric)
admin.site.register(LifespanGeneric)
admin.site.register(EntityType)
admin.site.register(LocationType)
