from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PaymentForm
from .models import Payment

def payment_list(request):
    """Vista para listar todos los pagos"""
    payments = Payment.objects.all().order_by('-date')
    return render(request, 'payments/payment_list.html', {'payments': payments})

def registrar_pago(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            messages.success(request, f'¡Pago registrado con éxito! Monto: ${payment.amount}')
            return redirect('pago_exitoso')
    else:
        form = PaymentForm()
    
    from django.utils import timezone
    context = {
        'form': form,
        'now': timezone.now(),
    }
    return render(request, 'payments/registrar_pago.html', context)

def pago_exitoso(request):
    return render(request, 'payments/pago_exitoso.html')

def imprimir_ticket(request, payment_id):
    """Vista para imprimir el ticket de un pago específico"""
    payment = get_object_or_404(Payment, id=payment_id)
    return render(request, 'payments/imprimir_ticket.html', {'payment': payment})
