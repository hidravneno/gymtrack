from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='reports_dashboard'),
    path('miembros/', views.member_reports, name='member_reports'),
    path('pagos/', views.payment_reports, name='payment_reports'),
    path('asistencias/', views.attendance_reports, name='attendance_reports'),
]
