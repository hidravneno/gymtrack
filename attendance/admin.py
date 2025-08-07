from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('member', 'check_in')
    search_fields = ('member__nombre', 'member__apellido')
    list_filter = ('check_in',)
