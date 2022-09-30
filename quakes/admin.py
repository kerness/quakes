from django.contrib import admin
from .models import Quake
from leaflet.admin import LeafletGeoAdmin


class QuakeAdmin(LeafletGeoAdmin):
    list_display = ['mag', 'date', 'vendor']

# class VendorAdmin(LeafletGeoAdmin):
#     list_display = ['name']

admin.site.register(Quake, QuakeAdmin)
# admin.site.register(DataVendor, VendorAdmin)
