from django.shortcuts import render
from django.db.models import Count, Sum, Avg
from django.utils import timezone
from datetime import timedelta, datetime
from members.models import Member, MembershipPlan
from attendance.models import Attendance
from payments.models import Payment

def dashboard(request):
    """Vista principal del panel de reportes"""
    # Obtener datos para el dashboard
    today = timezone.now().date()
    this_month_start = today.replace(day=1)
    
    # Estadísticas generales
    total_members = Member.objects.count()
    active_members = Member.objects.filter(plan__isnull=False).count()
    members_this_month = Member.objects.filter(fecha_inscripcion__gte=this_month_start).count()
    
    # Estadísticas de asistencia
    attendance_today = Attendance.objects.filter(check_in__date=today).count()
    attendance_this_month = Attendance.objects.filter(check_in__date__gte=this_month_start).count()
    
    # Estadísticas de pagos
    payments_today = Payment.objects.filter(date__date=today).aggregate(total=Sum('amount'))
    payments_this_month = Payment.objects.filter(date__date__gte=this_month_start).aggregate(total=Sum('amount'))
    
    # Datos para gráficos
    last_30_days = [today - timedelta(days=x) for x in range(30)]
    
    # Datos de asistencias por día (últimos 30 días)
    attendance_data = []
    for day in last_30_days:
        count = Attendance.objects.filter(check_in__date=day).count()
        attendance_data.append({
            'date': day.strftime('%d/%m'),
            'count': count
        })
    attendance_data.reverse()  # Ordenar de más antiguo a más reciente
    
    # Datos de pagos por día (últimos 30 días)
    payment_data = []
    for day in last_30_days:
        total = Payment.objects.filter(date__date=day).aggregate(total=Sum('amount'))['total'] or 0
        payment_data.append({
            'date': day.strftime('%d/%m'),
            'amount': float(total)
        })
    payment_data.reverse()  # Ordenar de más antiguo a más reciente
    
    context = {
        'total_members': total_members,
        'active_members': active_members,
        'members_this_month': members_this_month,
        'attendance_today': attendance_today,
        'attendance_this_month': attendance_this_month,
        'payments_today': payments_today['total'] or 0,
        'payments_this_month': payments_this_month['total'] or 0,
        'attendance_data': attendance_data,
        'payment_data': payment_data,
    }
    
    return render(request, 'reports/dashboard.html', context)

def member_reports(request):
    """Vista de reportes relacionados con miembros"""
    # Distribución por género
    gender_distribution = Member.objects.values('sexo').annotate(count=Count('id'))
    
    # Distribución por plan
    plan_distribution = Member.objects.values('plan__name').annotate(count=Count('id'))
    
    # Miembros por fecha de inscripción (por mes)
    today = timezone.now().date()
    months_back = 12
    months_data = []
    
    for i in range(months_back, 0, -1):
        month_date = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
        month_date = month_date.replace(month=((today.month - i) % 12) + 1)
        if month_date.month > today.month:
            month_date = month_date.replace(year=today.year - 1)
            
        next_month = month_date.replace(month=month_date.month % 12 + 1)
        if next_month.month == 1:
            next_month = next_month.replace(year=month_date.year + 1)
            
        count = Member.objects.filter(
            fecha_inscripcion__gte=month_date, 
            fecha_inscripcion__lt=next_month
        ).count()
        
        months_data.append({
            'month': month_date.strftime('%b %Y'),
            'count': count
        })
    
    # Miembros más activos (basados en asistencia)
    active_members = Attendance.objects.values('member__nombre', 'member__apellido').annotate(
        visits=Count('id')
    ).order_by('-visits')[:10]
    
    context = {
        'gender_distribution': gender_distribution,
        'plan_distribution': plan_distribution,
        'months_data': months_data,
        'active_members': active_members,
    }
    
    return render(request, 'reports/member_reports.html', context)

def payment_reports(request):
    """Vista de reportes relacionados con pagos"""
    # Filtrar por fecha si se proporciona
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    payments = Payment.objects.all()
    
    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        payments = payments.filter(date__date__gte=start_date)
        
    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        payments = payments.filter(date__date__lte=end_date)
    
    # Totales
    total_amount = payments.aggregate(total=Sum('amount'))['total'] or 0
    payment_count = payments.count()
    
    # Pagos por tipo
    payments_by_type = payments.values('payment_type').annotate(
        count=Count('id'),
        total=Sum('amount')
    ).order_by('-total')
    
    # Pagos por plan
    payments_by_plan = payments.values('plan__name').annotate(
        count=Count('id'),
        total=Sum('amount')
    ).order_by('-total')
    
    # Pagos por mes
    today = timezone.now().date()
    months_back = 12
    monthly_payments = []
    
    for i in range(months_back, 0, -1):
        month_date = today.replace(day=1)
        month_date = month_date.replace(month=((today.month - i) % 12) + 1)
        if month_date.month > today.month:
            month_date = month_date.replace(year=today.year - 1)
            
        next_month = month_date.replace(month=month_date.month % 12 + 1)
        if next_month.month == 1:
            next_month = next_month.replace(year=month_date.year + 1)
            
        month_total = Payment.objects.filter(
            date__date__gte=month_date, 
            date__date__lt=next_month
        ).aggregate(total=Sum('amount'))['total'] or 0
        
        monthly_payments.append({
            'month': month_date.strftime('%b %Y'),
            'amount': float(month_total)
        })
    
    context = {
        'total_amount': total_amount,
        'payment_count': payment_count,
        'payments_by_type': payments_by_type,
        'payments_by_plan': payments_by_plan,
        'monthly_payments': monthly_payments,
        'start_date': start_date.strftime('%Y-%m-%d') if start_date else '',
        'end_date': end_date.strftime('%Y-%m-%d') if end_date else '',
    }
    
    return render(request, 'reports/payment_reports.html', context)

def attendance_reports(request):
    """Vista de reportes relacionados con asistencias"""
    # Filtrar por fecha si se proporciona
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    attendances = Attendance.objects.all()
    
    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        attendances = attendances.filter(check_in__date__gte=start_date)
        
    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        attendances = attendances.filter(check_in__date__lte=end_date)
    
    # Totales
    attendance_count = attendances.count()
    
    # Asistencias por día de la semana
    weekdays = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    
    attendances_by_weekday = []
    for i, day in enumerate(weekdays, 1):
        # En Django, los días de la semana empiezan en 1 con domingo
        # Ajustamos para que 1 sea lunes
        django_day = i % 7 + 1
        count = attendances.filter(check_in__week_day=django_day).count()
        attendances_by_weekday.append({
            'day': day,
            'count': count
        })
    
    # Asistencias por hora del día
    attendances_by_hour = []
    for hour in range(24):
        count = attendances.filter(check_in__hour=hour).count()
        attendances_by_hour.append({
            'hour': f'{hour}:00',
            'count': count
        })
    
    # Asistencias por mes
    today = timezone.now().date()
    months_back = 12
    monthly_attendances = []
    
    for i in range(months_back, 0, -1):
        month_date = today.replace(day=1)
        month_date = month_date.replace(month=((today.month - i) % 12) + 1)
        if month_date.month > today.month:
            month_date = month_date.replace(year=today.year - 1)
            
        next_month = month_date.replace(month=month_date.month % 12 + 1)
        if next_month.month == 1:
            next_month = next_month.replace(year=month_date.year + 1)
            
        month_count = Attendance.objects.filter(
            check_in__date__gte=month_date, 
            check_in__date__lt=next_month
        ).count()
        
        monthly_attendances.append({
            'month': month_date.strftime('%b %Y'),
            'count': month_count
        })
    
    context = {
        'attendance_count': attendance_count,
        'attendances_by_weekday': attendances_by_weekday,
        'attendances_by_hour': attendances_by_hour,
        'monthly_attendances': monthly_attendances,
        'start_date': start_date.strftime('%Y-%m-%d') if start_date else '',
        'end_date': end_date.strftime('%Y-%m-%d') if end_date else '',
    }
    
    return render(request, 'reports/attendance_reports.html', context)
