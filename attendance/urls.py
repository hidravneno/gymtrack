from django.urls import path
from .views import registrar_asistencia, asistencia_exitosa, attendance_list

urlpatterns = [
    path('', attendance_list, name='attendance_list'),  # Lista de asistencias
    path('registrar/', registrar_asistencia, name='registrar_asistencia'),
    path('exito/', asistencia_exitosa, name='asistencia_exitosa'),
]
