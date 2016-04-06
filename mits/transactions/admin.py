from django.contrib import admin

from .models import GroupIssueFixed, GroupCheckOutLifespan, EmployeeIssueFixed, EmployeeCheckOutLifespan, ConsumableRequest, CateringRequest

admin.site.register(GroupIssueFixed)
admin.site.register(GroupCheckOutLifespan)
admin.site.register(EmployeeIssueFixed)
admin.site.register(EmployeeCheckOutLifespan)

class ConsumableRequestAdmin(admin.ModelAdmin):
	list_filter = ['request_date','status','requested_item','location']
	fieldsets = [
    	(None, {'fields': ['requestor']}),
    	('Request Information', {'fields': ['requested_item','location','status','notes']}),
    ]

#,'status'

admin.site.register(ConsumableRequest, ConsumableRequestAdmin)

class CateringRequestAdmin(admin.ModelAdmin):
	list_filter = ['status','request_date','delivery_date']
	fieldsets = [
    	(None, {'fields': ['requestor', 'request_date']}),
    	('Order Information', {'fields': ['vendor','head_count','location','delivery_date','status','notes']}),
    ]

#,'status'

admin.site.register(CateringRequest, CateringRequestAdmin)

