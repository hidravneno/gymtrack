from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_socio, name='registrar_socio'),
    path('exito/', views.registro_exitoso, name='registro_exitoso'),
    path('add/', views.add_member, name='add_member'),
    path('list/', views.member_list, name='member_list'),
    path('success/', views.member_success, name='member_success'),
    path('view/<int:member_id>/', views.view_member, name='view_member'),
    path('edit/<int:member_id>/', views.edit_member, name='edit_member'),
]
