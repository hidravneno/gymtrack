from django.db import models

class MembershipPlan(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_days = models.IntegerField(help_text="Duración del plan en días")

    def __str__(self):
        return self.name

class Member(models.Model):
    SEX_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1, choices=SEX_CHOICES)
    telefono = models.CharField(max_length=20)
    alergia = models.BooleanField(default=False)
    descripcion_alergia = models.CharField(max_length=200, blank=True)
    plan = models.ForeignKey(MembershipPlan, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    observaciones = models.TextField(blank=True, max_length=300)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
