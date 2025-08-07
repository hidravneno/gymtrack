from django import forms
from .models import Attendance
from members.models import Member

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['member']
