from django.contrib import admin

from .models import Spot


@admin.register(Spot)
class SpotAdmin(admin.ModelAdmin):
    list_display = ('author', 'latitude', 'longitude', 'created', 'colour')
