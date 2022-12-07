from django.shortcuts import render
from aplicacion1.forms import FormAuto
from aplicacion1.forms import FormRRHH
from aplicacion1.forms import FormCliente
from aplicacion1.models import Auto
from aplicacion1.models import PersonalRRHH
from aplicacion1.models import Cliente
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return render(request,'index.html')

def listadoAutos(request):
    autos = Auto.objects.all()
    data  = {'autos' : autos}
    return render(request, 'autos.html',data)

def agregarAuto(request):
    form = FormAuto()
    if request.method == 'POST':
        form = FormAuto(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request,'agregarAutos.html',data)

def eliminaRRHH(request,id):
    eliminar = PersonalRRHH.objects.get(id = id)
    eliminar.delete()
    return redirect('/ListadoRRHH.html')


def eliminarAuto(request,id):
    objeliminar = Auto.objects.get(id = id)
    objeliminar.delete()
    return redirect('/Listado')



def actualizarAuto(request, id):
    autoo = Auto.objects.get(id = id)
    form = FormAuto(instance=autoo)
    if request.method == 'POST':
        form = FormAuto(request.POST, instance=autoo)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request,'agregarAutos.html',data)

def listadoRRHH(request):
    rrhh = PersonalRRHH.objects.all()
    data  = {'rrhh' : rrhh}
    return render(request,'ListadoRRHH.html',data)

def agregarRRHH(request):
    form = FormRRHH()
    if request.method == 'POST':
        form = FormRRHH(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request,'agregarRRHH.html',data)

def actualizarRRHH(request, id):
    rrhh = PersonalRRHH.objects.get(id = id)
    form = FormRRHH(instance=rrhh)
    if request.method == 'POST':
        form = FormRRHH(request.POST, instance=rrhh)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request,'agregarRRHH.html',data)

def eliminaRRHH(request,id):
    eliminar = PersonalRRHH.objects.get(id = id)
    eliminar.delete()
    return redirect('../ListadoRRHH/')

def listadoCliente(request):
    listado = Cliente.objects.all()
    data  = {'listado' : listado}
    return render(request,'listadocliente.html',data)

def agregarcliente(request):
    form = FormCliente()
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request,'agregarCliente.html',data)

def eliminaCliente(request,id):
    eliminar = Cliente.objects.get(id = id)
    eliminar.delete()
    return redirect('../listadocliente/')

def actualizarCliente(request, id):
    clente = Cliente.objects.get(id = id)
    form = FormCliente(instance=clente)
    if request.method == 'POST':
        form = FormCliente(request.POST, instance=clente)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request,'agregarCliente.html',data)