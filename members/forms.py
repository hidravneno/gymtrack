from django import forms
from .models import Member, MembershipPlan
from payments.models import Payment
from attendance.models import Attendance

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['nombre', 'apellido', 'edad', 'sexo', 'telefono', 'alergia', 'descripcion_alergia', 'plan', 'observaciones']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['member', 'amount', 'plan']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['member']
