from django.shortcuts import render


#IMPORTAR EL FORMULARIO A RENDER
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioempleados import formularioEmpleados

from web.models import Platos

# Create your views here.
#las vistas en djangp son los CONTROLADORES

#las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

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

def VistaPersonal(request):
        formulario=formularioEmpleados()
        datosParaTemplate={
            'formularioEmpleados':formulario,
        }
        return render(request,'personal.html',datosParaTemplate)
        

