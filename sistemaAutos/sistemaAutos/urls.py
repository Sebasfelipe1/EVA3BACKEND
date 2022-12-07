"""sistemaAutos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicacion1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    ##AUTOS
    path('Listado/', views.listadoAutos),
    path('agregarAutos/', views.agregarAuto),
    path('eliminarAutos/ <int:id>', views.eliminarAuto),
    path('actualizarAuto/ <int:id>', views.actualizarAuto),
    
    ##RECURSOS HUMANOS
    path('ListadoRRHH/', views.listadoRRHH),
    path('agregarRRHH/', views.agregarRRHH),
    path('actualizarRRHH/ <int:id>', views.actualizarRRHH),
    path('eliminarRRHH/ <int:id>', views.eliminaRRHH),
    
    
    ##CLIENTE
    path('listadocliente/', views.listadoCliente),
    path('agregarCliente/',views.agregarcliente),
    path('eliminarCliente/ <int:id>', views.eliminaCliente),
    path('actualizarCliente/ <int:id>', views.actualizarCliente),
    
]
