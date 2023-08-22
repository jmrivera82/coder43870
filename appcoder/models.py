from django.db import models

# Create your models here.

class oficinas(models.Model):
    nombre=models.CharField(max_length=50)
    ubicacion=models.CharField(max_length=50)
    #def __str__(self):
    #    return f"{self.nombre} - {self.ubicacion}"
    

class personal(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email} - {self.telefono}"


class equipos(models.Model):
    codigo=models.CharField(max_length=13)
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    tipo=models.CharField(max_length=20)
    usuario=models.CharField(max_length=50)
    fecha_ingreso=models.DateTimeField()
    
    def __str__(self):
        return f"{self.codigo} - {self.marca} - {self.modelo} - {self.tipo} - {self.usuario} - {self.fecha_ingreso}"


class trabajos(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()
    
    def __str__(self):
        return f"{self.nombre} - {self.fecha_entrega} - {self.entregado}"

#trabajo de clases


class curso(models.Model):

    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()
    

class estudiantes(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    

class profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    profesion=models.CharField(max_length=50)
    
#class entregable(models.Model):
 #   nombre=models.CharField(max_length=50)
#    fecha_entrega=models.DateField()
#    entregado=models.BooleanField()
    
