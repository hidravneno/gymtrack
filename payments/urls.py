from django.urls import path
from .views import registrar_pago, pago_exitoso, payment_list, imprimir_ticket

urlpatterns = [
    path('', payment_list, name='payment_list'),  # Lista de pagos
    path('registrar/', registrar_pago, name='registrar_pago'),
    path('exito/', pago_exitoso, name='pago_exitoso'),
    path('imprimir/<int:payment_id>/', imprimir_ticket, name='imprimir_ticket'),
]
