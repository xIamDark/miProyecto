from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    id_producto = models.AutoField(db_column='id_producto', primary_key=True)
    tipo    = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self):
        return str(self.tipo)
    
class Producto(models.Model):
    codigo        = models.CharField(primary_key=True, max_length=10)
    tipo_producto = models.ForeignKey('TipoProducto',on_delete=models.CASCADE, db_column='id_producto')
    nombre        = models.CharField(max_length=20)
    fecha_llegada = models.DateField(blank=False, null=False)
    cantidad      = models.IntegerField()
    
    def __str__(self):
        return str(self.codigo)+" = "+str(self.nombre)+" ,llego el ("+str(self.fecha_llegada)+")" 