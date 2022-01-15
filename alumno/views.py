from django.shortcuts import render,redirect
from .forms import AlumnoForm
from .models import Alumno

# Create your views here.

def alumno(request):
    data=Alumno.objects.all()
    return render(request,'alumno.html',{'data':data})

def CrearAlumno(request):
    formulario = AlumnoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('alumnos')
    return render(request,'crear_alumno.html',{'formulario':formulario})

def eliminarAlumno(request,id):
    alumno=Alumno.objects.get(id=id)

    alumno.delete()

    return redirect('alumnos')

def modificarAlumno(request,id):
    alumno=Alumno.objects.get(id=id)

    formulario=AlumnoForm(request.POST or None, request.FILES or None, instance=alumno)

    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('alumnos')

    return render(request,'modificar.html',{'formulario':formulario})