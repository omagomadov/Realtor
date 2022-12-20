from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import UserForm
from odoo.auth.xml_rpc import connect
from .models import User

def index(request):
    return render(request, 'auth_odoo/index.html', {'form' : UserForm})

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    
    if connect(email, password, 'dev01'):
        if not User.objects.filter(email = email).exists():
            User.objects.create_user(email = email, password = password)

        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
    
    return redirect('auth_odoo:index')

def logout(request):
    auth_logout(request)

    return redirect('auth_odoo:index')