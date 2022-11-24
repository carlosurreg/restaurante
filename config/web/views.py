from django.shortcuts import render, redirect


#IMPORTAR EL FORMULARIO A RENDER
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioempleados import formularioEmpleados
from web.formularios.formularioEditarPlato import FormularioEditarPlatos
from web.formularios.formularioEditarEmpleado import FormularioEditarEmpleados

from web.models import Platos, Empleados

# Create your views here.
#las vistas en djangp son los CONTROLADORES

#las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

def empleados(request):
    empleadosConsultados = Empleados.objects.all()
    formulario = FormularioEditarEmpleados()
    diccionarioEnviado = {
        'empleados' : empleadosConsultados,
        'formulario' : formulario
    }
    return render(request, 'empleados.html', diccionarioEnviado)

def MenuPlatos(request):
    platosConsultados = Platos.objects.all()
    formulario = FormularioEditarPlatos()
    diccionarioEnvio = {
        'platos' : platosConsultados,
        'formulario' : formulario
    }
    return render(request, 'menuPlatos.html', diccionarioEnvio)


def EditarPlato(request, id):
    #Recibir los datos del formulario y editar mi plato
    print(id)
    if request.method == 'POST':
        datosDelFormulario = FormularioEditarPlatos(request.POST)
        if datosDelFormulario.is_valid():
            datosPlato = datosDelFormulario.cleaned_data
            try:
                Platos.objects.filter(pk = id).update(precio = datosPlato["precioPlato"])
                print("EXITO GUARDANDO LOS DATOS")
            except Exception as error:
                print("error",error)
    return redirect('menu')

def EditarEmpleado(request, id):
    print(id)
    if request.method == 'POST':
        datosDelFormulario = FormularioEditarEmpleados(request.POST)
        if datosDelFormulario.is_valid():
            datosEmpleado = datosDelFormulario.cleaned_data
            try:
                Empleados.objects.filter(pk = id).update(salario = datosEmpleado["salarioEmpleados"])
                Empleados.objects.filter(pk = id).update(contacto = datosEmpleado["contactoEmpleados"])
                print("EXITO GUARDANDO LOS DATOS")
            except Exception as error:
                print("error", error)
    return redirect('empleados')


def VistaEmpleados(request):
    formulario = formularioEmpleados()
    datosParaTemples = {
        'formularioRegistro':formulario,
        'bandera':False
    }
    if request.method == 'POST':
        datosDelFormulario = formularioEmpleados(request.POST)
        if datosDelFormulario.is_valid():
            datosEmpleados = datosDelFormulario.cleaned_data
            empleadosNuevo = Empleados(
                nombres = datosEmpleados["nombresEmpleados"],
                apellidos = datosEmpleados["apellidosEmpleados"],
                foto = datosEmpleados["fotoEmpleados"],
                cargo = datosEmpleados["cargoEmpleados"],
                salario = datosEmpleados["salarioEmpleados"],
                contacto = datosEmpleados["contactoEmpleados"],
            )
            try:
                empleadosNuevo.save()
                datosParaTemples["bandera"] = True
                print("EXITO GUARDANDO LOS DATOS")
            
            except Exception as error:
                datosParaTemples["bandera"] = False
                print("error", error)
    return render(request, 'empleados.html', datosParaTemples)



def VistaPlatos(request):

    formulario=FormularioPlatos()
    datosParaTemplate={
        'formularioRegistro':formulario,
        'bandera':False
    }

    #PREGUNTAMOS SI EXISTE ALGUNA CONEXION DE TIPO POST ASOCIADA A LA VISTA
    if request.method=="POST":
        #deberiamos capturar los datos del formulario|
        datosDelFromulario=FormularioPlatos(request.POST)
        #verificar si los datos llegaron correctamente (VALIDACIONES OK)
        if datosDelFromulario.is_valid():
            #capturamos la data 
            datosPlato=datosDelFromulario.cleaned_data
            #creamos un objeto del tipo MODELO PLATO
            platoNuevo=Platos(
                nombre=datosPlato["nombrePlato"],
                descripcion=datosPlato["descripcionPlato"],
                foto=datosPlato["fotoPlato"],
                precio=datosPlato["precioPlato"],
                tipo=datosPlato["tipoPlato"], 
            )
            #Intentamos llevar el objeto platoNuevo a la BD
            try:
                platoNuevo.save()
                datosParaTemplate["bandera"]=True
                print("EXITO GUARDANDO LOS DATOS")

            except Exception as error:
                datosParaTemplate["bandera"]=False
                print("error",error)


    return render(request,'platos.html',datosParaTemplate)


        

