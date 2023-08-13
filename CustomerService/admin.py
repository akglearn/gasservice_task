from django.contrib import admin
from .models import ServiceRequest, Customer

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('type', 'status', 'submitted_at', 'resolved_at')
    list_filter = ('type', 'status')
    search_fields = ('details',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_number', 'address')
    search_fields = ('user__username', 'contact_number')
