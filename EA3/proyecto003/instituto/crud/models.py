from django.db import models

# Create your models here.

class Marca(models.Model):
    idMarca = models.AutoField(db_column='idMarca', primary_key=True)
    nombre = models.CharField(db_column='nombre', max_length=50, null=False)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre
# PASOS:
# 1.- para preparar la migración:
# py manage.py makemigrations crud
# 2.- hacer migracion
# py manage.py migrate crud

### otras clases que representan los modelos