from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AttendanceForm
from .models import Attendance
from django.utils import timezone
from datetime import timedelta

def attendance_list(request):
    """Vista para listar todas las asistencias"""
    # Por defecto, mostrar las asistencias del día actual
    today = timezone.now().date()
    attendances = Attendance.objects.filter(check_in__date=today).order_by('-check_in')
    
    context = {
        'attendances': attendances,
        'current_date': today,
    }
    return render(request, 'attendance/attendance_list.html', context)

def registrar_asistencia(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save()
            messages.success(request, f'¡Se ha registrado con éxito la asistencia de {attendance.member.nombre} {attendance.member.apellido}!')
            return redirect('asistencia_exitosa')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/registrar_asistencia.html', {'form': form})

def asistencia_exitosa(request):
    from django.utils import timezone
    context = {
        'now': timezone.now(),
    }
    return render(request, 'attendance/asistencia_exitosa.html', context)
