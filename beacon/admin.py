from django.contrib import admin
from .models import Beacon
# Register your models here.


class BeaconAdmin(admin.ModelAdmin):
    list_display = ("minor_value", "lecturer", "subject",)


admin.site.register(Beacon, BeaconAdmin)
