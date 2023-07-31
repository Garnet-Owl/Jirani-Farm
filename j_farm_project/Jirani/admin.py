# Register your models here.
from django.contrib import admin
from .models import Farmer, Tractor, Lease

# Register your models here.

admin.site.register(Farmer)
admin.site.register(Tractor)
admin.site.register(Lease)
