from django.shortcuts import render, redirect
from odoo.auth.xml_rpc import fetch as retrieve_datat, connect as auth

def index(request):
    if not request.user.is_authenticated:
        return redirect('auth_odoo:index')
    else:
        products = retrieve_datat(request.user.email, request.user.password_odoo, 'dev01')
        return render(request, 'apartments/apartments.html', {'products' : products})

def offer(request):
    return render(request, 'apartments/apartments.html')