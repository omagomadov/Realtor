from django.shortcuts import render, redirect
from odoo.auth.xml_rpc import fetch as retrieve_datat

def index(request):
    if not request.user.is_authenticated:
        return redirect('auth_odoo:index')
    else:
        return render(request, 'apartments/apartments.html')

def fetch(request):
    products = retrieve_datat(request.user.email, request.POST['password'], 'dev01')
    return render(request, 'apartments/apartments.html', {'products' : products})