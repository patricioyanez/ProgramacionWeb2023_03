from django.db import models

# Create your models here.

class Marca(models.Model):
    idMarca = models.AutoField(db_column='idMarca', primary_key=True)
    nombre = models.CharField(db_column='nombre', max_length=50, null=False)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre
    

class Categoria(models.Model):
    idCategoria = models.AutoField(db_column='idCategoria', primary_key=True)
    nombre = models.CharField(db_column='nombre', max_length=50, null=False, unique=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre
    

class Genero(models.Model):
    idGenero = models.AutoField(db_column='idGenero', primary_key=True)
    nombre = models.CharField(db_column='nombre', max_length=50, null=False, unique=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre
    

class Cliente(models.Model):
    idCliente = models.AutoField(db_column='idCliente', primary_key=True)
    rut = models.IntegerField(unique=True, null=False, blank=False)
    dv = models.CharField(max_length=1, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    telefono = models.CharField(max_length=50, null=False, blank=False)
    genero = models.ForeignKey(Genero, db_column='idGenero', 
                                        on_delete=models.CASCADE, null=False, blank=False)
    fechaNacimiento = models.DateField(null=False, blank=False)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre
    


# PASOS:
# 1.- para preparar la migración:
# py manage.py makemigrations crud
# 2.- hacer migracion
# py manage.py migrate crud

### otras clases que representan los modelos