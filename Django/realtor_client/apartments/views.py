from django.shortcuts import render, redirect
from odoo.auth.xml_rpc import fetch as retrieve_data, submit as submit_offer

def index(request):
    if not request.user.is_authenticated:
        return redirect('auth_odoo:index')
    else:
        products = retrieve_data(request.user.email, request.user.password_odoo, 'dev01')
        return render(request, 'apartments/apartments.html', {'products' : products})

def offer(request):
    submit_offer(request.user.email, request.user.password_odoo, 'dev01', request.GET['buyer'], request.GET['amount'], request.GET['apartment_name'])
    return redirect('apartments:index')