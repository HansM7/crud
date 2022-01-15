from django.urls import path

from . import views

urlpatterns = [
    path("",views.alumno, name="alumnos"),
    path("alumno/crear_alumno", views.CrearAlumno, name="crear_alumno"),
    path("eliminar/<int:id>/", views.eliminarAlumno, name="eliminar"),
    path("modificar/<int:id>/", views.modificarAlumno, name="modificar"),
]

