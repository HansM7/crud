from django.db import models

# Create your models here.
class Alumno(models.Model):
    imagen=models.ImageField(upload_to='Alumnos')

    nombre=models.TextField(max_length=200)
    celular=models.TextField(max_length=10)

    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
    
    def delete(self):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()