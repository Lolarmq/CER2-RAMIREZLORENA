from django.db import models

# Create your models here.
class Categoria(models.Model):

    nombre = models.CharField(max_length = 100)
    descripcion = models.TextField()
    imagen = models.URLField(blank = True)

    def __str__(self):
        return self.nombre

class LugarPatrimonial(models.Model):

    nombre = models.CharField(max_length = 150)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length = 200)
    anio_construccion = models.IntegerField()
    imagen = models.URLField()

    categoria = models.ForeignKey('Categoria',on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre