from django.contrib import admin
from .models import Quake
from leaflet.admin import LeafletGeoAdmin


class QuakeAdmin(LeafletGeoAdmin):
    list_display = ['mag', 'date']

admin.site.register(Quake, QuakeAdmin)
