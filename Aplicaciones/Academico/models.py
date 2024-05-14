from django.db import models
import datetime

# Create your models here.

class Cliente(models.Model):
    idCliente=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre,self.apellido)

class Entrenador(models.Model):
    idEntrenador=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono=models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre,self.apellido)

class Clase(models.Model):
    idClase=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    dia=models.CharField(max_length=50)
    horario=models.CharField(max_length=15)
    fecha=models.DateField()
    costoCuotas=models.FloatField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre)


class Caja(models.Model):
    idCaja=models.CharField(primary_key=True, max_length=6)
    tipo=models.CharField(max_length=20)
    monto=models.FloatField()
    fecha=models.DateField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.tipo)
    

class Productos(models.Model):
    idProducto=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=20)
    stock=models.CharField(max_length=20)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre)

class Facturas(models.Model):
    numFac=models.CharField(primary_key=True, max_length=6)
    nombreFac=models.CharField(max_length=20)
    fecha=models.DateField()
    importe=models.FloatField()
    idCaja=models.ForeignKey(Caja,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombreFac)
    
class Rutinas(models.Model):
    idRutina=models.CharField(primary_key=True, max_length=6)
    ejercicio=models.CharField(max_length=20)
    cantidad=models.IntegerField()
    fecha=models.DateField()
    idCliente=models.ForeignKey(Cliente,null=True,blank=True,on_delete=models.CASCADE)
    idEntrenador=models.ForeignKey(Entrenador,null=True,blank=True,on_delete=models.CASCADE)

class Recibos(models.Model):
    numRecibo=models.CharField(primary_key=True, max_length=6)
    sueldo=models.FloatField()
    fecha=models.DateField()
    idEntrenador=models.ForeignKey(Entrenador,null=True,blank=True,on_delete=models.CASCADE)

class clientesXclases (models.Model):
    idCxC=models.CharField(primary_key=True, max_length=6)
    fecha=models.DateField()
    estado=models.CharField(max_length=30)
    idCliente=models.ForeignKey(Cliente,null=True,blank=True,on_delete=models.CASCADE)
    idClase=models.ForeignKey(Clase,null=True,blank=True,on_delete=models.CASCADE)
    

class Cobro (models.Model):
    idCobro=models.CharField(primary_key=True, max_length=6)
    idCliente=models.ForeignKey(Cliente,null=True,blank=True,on_delete=models.CASCADE)
    idClase=models.ForeignKey(Clase,null=True,blank=True,on_delete=models.CASCADE)
    CostoCuota=models.FloatField()
    fecha=models.DateField()


class alumnoXclase (models.Model):
    idAxC=models.CharField(primary_key=True, max_length=6)