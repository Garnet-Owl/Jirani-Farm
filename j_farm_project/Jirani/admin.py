# Register your models here.
from django.contrib import admin
from .models import Farmer, Tractor, Lease

# Register your models here.

class FarmerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'location')

class TractorAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'price', 'available', 'owner')

class LeaseAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'status', 'tractor', 'renter')

admin.site.register(Farmer, FarmerAdmin),
admin.site.register(Tractor, TractorAdmin),
admin.site.register(Lease, LeaseAdmin),
