from django.shortcuts import render

def index(request):
    return render(request, 'apartments/apartments.html')
