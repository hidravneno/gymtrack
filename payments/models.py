from django.db import models
from members.models import Member, MembershipPlan

class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta de Crédito/Débito'),
        ('transferencia', 'Transferencia Bancaria'),
        ('otro', 'Otro'),
    ]
    
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    plan = models.ForeignKey(MembershipPlan, on_delete=models.SET_NULL, null=True)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES, default='efectivo', verbose_name="Tipo de Pago")
    notes = models.TextField(blank=True, null=True, verbose_name="Notas")

    def __str__(self):
        return f"{self.member.nombre} {self.member.apellido} pagó ${self.amount} el {self.date.strftime('%d/%m/%Y')}"
