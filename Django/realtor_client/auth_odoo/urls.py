from django.urls import path, include
from . import views


app_name = 'auth_odoo'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]