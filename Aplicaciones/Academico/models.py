
from django.db import models
import datetime

# Create your models here.

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.apellido)

class Entrenador(models.Model):
    idEntrenador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.apellido)

class Clase(models.Model):
    idClase = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    dia = models.CharField(max_length=50)
    horario = models.CharField(max_length=15)
    fecha = models.DateField()
    costoCuotas = models.FloatField()

    def __str__(self):
        return self.nombre

class Caja(models.Model):
    idCaja = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20)
    monto = models.FloatField()
    fecha = models.DateField()

    def __str__(self):
        return self.tipo

class Productos(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    stock = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Facturas(models.Model):
    numFac = models.AutoField(primary_key=True)
    nombreFac = models.CharField(max_length=20)
    fecha = models.DateField()
    importe = models.FloatField()
    idCaja = models.ForeignKey(Caja, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreFac

class Rutinas(models.Model):
    idRutina = models.AutoField(primary_key=True)
    ejercicio = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    idCliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    idEntrenador = models.ForeignKey(Entrenador, null=True, blank=True, on_delete=models.CASCADE)

class Recibos(models.Model):
    numRecibo = models.AutoField(primary_key=True)
    sueldo = models.FloatField()
    fecha = models.DateField()
    idEntrenador = models.ForeignKey(Entrenador, null=True, blank=True, on_delete=models.CASCADE)

class clientesXclases(models.Model):
    idCxC = models.AutoField(primary_key=True)
    fecha = models.DateField()
    estado = models.CharField(max_length=30)
    idCliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    idClase = models.ForeignKey(Clase, null=True, blank=True, on_delete=models.CASCADE)

class Cobro(models.Model):
    idCobro = models.AutoField(primary_key=True)
    idCliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    idClase = models.ForeignKey(Clase, null=True, blank=True, on_delete=models.CASCADE)
    CostoCuota = models.FloatField()
    fecha = models.DateField()

class alumnoXclase(models.Model):
    idAxC = models.AutoField(primary_key=True)
