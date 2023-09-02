from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # No powershell
    # python .\manage.py migrate
    # python .\manage.py runserver
]