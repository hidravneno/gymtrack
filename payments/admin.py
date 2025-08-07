from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('member', 'amount', 'plan', 'payment_type', 'date')
    search_fields = ('member__nombre', 'member__apellido', 'notes')
    list_filter = ('plan', 'payment_type', 'date')
