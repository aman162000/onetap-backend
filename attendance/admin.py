from django.contrib import admin
from .models import Attendance
# Register your models here.


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "is_present", "beacon",)

    readonly_fields = ("beacon",)


admin.site.register(Attendance, AttendanceAdmin)
