from django.shortcuts import render

def home(request):
    """Vista para la página principal del gimnasio"""
    return render(request, 'home.html')
