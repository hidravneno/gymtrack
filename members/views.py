from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import MemberForm
from .models import Member

def registrar_socio(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')
    else:
        form = MemberForm()
    return render(request, 'members/registrar_socio.html', {'form': form})

def registro_exitoso(request):
    return render(request, 'members/registro_exitoso.html')

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Miembro agregado exitosamente.')
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'members/add_member.html', {'form': form})

def member_success(request):
    return render(request, 'members/member_success.html')

def member_list(request):
    members = Member.objects.all().order_by('-fecha_inscripcion')
    return render(request, 'members/member_list.html', {'members': members})

def view_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    return render(request, 'members/view_member.html', {'member': member})

def edit_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Miembro actualizado exitosamente.')
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'members/edit_member.html', {'form': form, 'member': member})
