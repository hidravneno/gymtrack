from django.contrib import admin
from .models import Member, MembershipPlan

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'plan', 'fecha_inscripcion')
    search_fields = ('nombre', 'apellido', 'telefono')
    list_filter = ('plan', 'sexo')

@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_days')
    search_fields = ('name',)
    list_filter = ('duration_days',)
