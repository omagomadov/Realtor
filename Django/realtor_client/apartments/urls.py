from django.urls import path
from . import views


app_name = 'apartments'

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch/', views.fetch, name='fetch'),
]