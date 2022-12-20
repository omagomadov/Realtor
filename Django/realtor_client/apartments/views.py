from django.shortcuts import render, redirect

def index(request):
    if not request.user.is_authenticated:
        return redirect('auth_odoo:index')
    else:
        return render(request, 'apartments/apartments.html')
