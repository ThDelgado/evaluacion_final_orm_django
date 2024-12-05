from django.db import models
from django.utils import timezone

# Create your models here.


class Laboratorio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50, blank=False, null=False,  default="Sin pais")
    ciudad = models.CharField(max_length=50, blank=False, null=False, default="Sin ciudad")
    imagen = models.URLField(null=True)


    class Meta:
        managed = True
        db_table = 'laboratorio'
    
    def __str__(self):
        return self.nombre
    
    
class DirectorGeneral(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100, blank=False, null=False, default="Sin especialidad")

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 'director'
     

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    p_costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    f_fabricacion = models.DateField(blank=True, null=True,default= timezone.now)
    imagen = models.URLField(null=True)
    laboratorio = models.ForeignKey('Laboratorio', on_delete= models.CASCADE)

    class Meta:
        managed = True
        db_table = 'producto'

    def __str__(self):
        return self.nombre
    