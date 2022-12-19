from django.urls import path, include
from . import views


app_name = 'auth_odoo'

urlpatterns = [
    path('', views.index, name='index'),
]