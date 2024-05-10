from django.db import models

# Create your models here.
class Camion(models.Model):
    patente_camion = models.CharField(max_length=6, null=True)
    conductor = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'Camiones'

    def __str__(self):
        return self.patente_camion 

class Despacho(models.Model):
    fecha = models.DateField( null=True)
    patente_camion = models.ForeignKey(Camion, on_delete=models.PROTECT, null=True)
    intento = models.IntegerField(default=0)
    entrgado = models.BooleanField(default=False)

    class Meta:
        db_table = 'Despacho'





class Resumen_Despacho(models.Model):
    id_venta = models.IntegerField()
    id_despacho = models.IntegerField()

    class Meta:
        db_table = 'Resumen_Despacho'
