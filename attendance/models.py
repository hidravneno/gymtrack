from django.db import models
from members.models import Member

class Attendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    check_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.nombre} {self.member.apellido} ingresó el {self.check_in.strftime('%d/%m/%Y %H:%M')}"
