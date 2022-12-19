from django.shortcuts import render

def index(request):
    return render(request, 'auth_odoo/index.html')
