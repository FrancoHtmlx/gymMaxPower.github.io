from django.shortcuts import render, redirect
from .models import Cliente,Entrenador,Clase,Caja,Productos,Facturas,Rutinas,Recibos,clientesXclases,Cobro,alumnoXclase
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def home(request):
    cliente = Cliente.objects.all()
    messages.success(request, '¡Clientes Listados!')
    return render(request, "gestionCliente.html", {"cliente": cliente})
#minuto 28 del video
def signup(request):

    if request.method == 'GET':
         return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #register User
            try:
                user = User.objects.create_user(username=request.POST['username'], 
                password=request.POST['password1'])
                user.save()
                return HttpResponse('User create successfully')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm
                    
                })
        return render(request, 'signup.html', {
                'form': UserCreationForm
                
        })
        

   

def entrenadores(request):
    entrenadores = Entrenador.objects.all()
    messages.success(request, '¡Entrenadores Listados!')
    return render(request, "gestionEntrenador.html", {"entrenadores": entrenadores})

def registrarEntrenador(request):
    idEntrenador=request.POST['txtidEntrenador']
    Nombre=request.POST['txtNombre']
    Apellido=request.POST['txtApellido']
    Telefono=request.POST['txtTelefono']
    Direccion=request.POST['txtDireccion']

    entrenador = Entrenador.objects.create(idEntrenador=idEntrenador, nombre=Nombre, apellido=Apellido,
    telefono=Telefono,direccion=Direccion)
    messages.success(request, 'Entrenador Registrado!')
    return redirect('/entrenadores')

def edicionEntrenador(request, idEntrenador):
    entrenadores = Entrenador.objects.get(idEntrenador=idEntrenador)
    return render(request, "edicionEntrenador.html", {"entrenadores": entrenadores})

def editarEntrenador(request):
    idEntrenador=request.POST['txtidEntrenador']
    Nombre=request.POST['txtNombre']
    Apellido=request.POST['txtApellido']
    Telefono=request.POST['txtTelefono']
    Direccion=request.POST['txtDireccion']

    entrenadores = Entrenador.objects.get(idEntrenador=idEntrenador)
    entrenadores.idEntrenador = idEntrenador
    entrenadores.nombre = Nombre
    entrenadores.apellido = Apellido
    entrenadores.telefono = Telefono
    entrenadores.direccion = Direccion
    entrenadores.save()

    messages.success(request, 'Entrenador Actualizado!')

    return redirect('/entrenadores')

def eliminarEntrenador(request, idEntrenador):
    entrenadores = Entrenador.objects.get(idEntrenador=idEntrenador)
    entrenadores.delete()

    messages.success(request, 'Entrenador Eliminado!')

    return redirect('/entrenadores')

#clases = Clase.objects.filter(estado='activo')

def clases(request):
    clases = Clase.objects.all()
    messages.success(request, '¡Clases Listados!')
    return render(request, "gestionClase.html", {"clases": clases})

def registrarClase(request):
    idClase=request.POST['txtidClase']
    Nombre=request.POST['txtNombre']
    Dia=request.POST['txtDia']
    Horario=request.POST['txtHorario']
    Fecha=request.POST['dateFecha']
    CostoCuotas=request.POST['floatCostoCuotas']

    clase = Clase.objects.create(idClase=idClase, nombre=Nombre, dia=Dia,
    horario=Horario,fecha=Fecha,costoCuotas=CostoCuotas)
    messages.success(request, 'Clase Registrada!')
    return redirect('/clases')

def edicionClase(request, idClase):
    clases = Clase.objects.get(idClase=idClase)
    return render(request, "edicionClase.html", {"clases": clases})

def editarClase(request):
    idClase=request.POST['txtidClase']
    Nombre=request.POST['txtNombre']
    Dia=request.POST['txtDia']
    Horario=request.POST['txtHorario']
    Fecha=request.POST['dateFecha']
    CostoCuotas=request.POST['floatCostoCuotas']

    clases = Clase.objects.get(idClase=idClase)
    clases.idClase = idClase
    clases.nombre = Nombre
    clases.dia = Dia
    clases.horario = Horario
    clases.fecha = Fecha
    clases.save()

    messages.success(request, 'Clase Actualizada!')

    return redirect('/clases')

def eliminarClase(request, idClase):
    clases = Clase.objects.get(idClase=idClase)
    clases.delete()

    messages.success(request, 'Clase Eliminada!')

    return redirect('/clases')

def cajas(request):
    cajas = Caja.objects.all()
    messages.success(request, '¡Caja Listadas!')
    return render(request, "gestionCaja.html", {"cajas": cajas})

def registrarCaja(request):
    idCaja=request.POST['txtidCaja']
    Tipo=request.POST['txtTipo']
    Monto=request.POST['floatMonto']
    Fecha=request.POST['dateFecha']

    caja = Caja.objects.create(idCaja=idCaja, tipo=Tipo, monto=Monto,
    fecha=Fecha)
    messages.success(request, 'Caja Registrada!')
    return redirect('/cajas')

def edicionCaja(request, idCaja):
    cajas = Caja.objects.get(idCaja=idCaja)
    return render(request, "edicionCaja.html", {"cajas": cajas})

def editarCaja(request):
    idCaja=request.POST['txtidCaja']
    Tipo=request.POST['txtTipo']
    Monto=request.POST['floatMonto']
    Fecha=request.POST['dateFecha']

    cajas = Caja.objects.get(idCaja=idCaja)
    cajas.idCaja = idCaja
    cajas.tipo = Tipo
    cajas.monto = Monto
    cajas.fecha = Fecha
    cajas.save()

    messages.success(request, 'Caja Actualizada!')

    return redirect('/cajas')

def eliminarCaja(request, idCaja):
    cajas = Caja.objects.get(idCaja=idCaja)
    cajas.delete()

    messages.success(request, 'Caja Eliminada!')

    return redirect('/cajas')


def productos(request):
    productos = Productos.objects.all()
    messages.success(request, '¡Productos Listados!')
    return render(request, "gestionProductos.html", {"productos": productos})

def registrarProducto(request):
    idProducto=request.POST['txtidProducto']
    Nombre=request.POST['txtNombre']
    Stock=request.POST['txtStock']

    productos = Productos.objects.create(idProducto=idProducto, nombre=Nombre, stock=Stock)
    messages.success(request, 'Producto Registrado!')
    return redirect('/productos')

def edicionProducto(request, idProducto):
    productos = Productos.objects.get(idProducto=idProducto)
    return render(request, "edicionProductos.html", {"productos": productos})

def editarProducto(request):
    idProducto=request.POST['txtidProducto']
    Nombre=request.POST['txtNombre']
    Stock=request.POST['txtStock']

    productos = Productos.objects.get(idProducto=idProducto)
    productos.idProducto = idProducto
    productos.nombre = Nombre
    productos.stock = Stock
    productos.save()

    messages.success(request, 'Producto Actualizado!')

    return redirect('/productos')

def eliminarProducto(request, idProducto):
    productos = Productos.objects.get(idProducto=idProducto)
    productos.delete()

    messages.success(request, 'Producto Eliminado!')

    return redirect('/productos')

def facturas(request):
    facturas = Facturas.objects.all()
    #print(str(facturas))
    cajas = Caja.objects.all()
    messages.success(request, 'Facturas Listadas!')
    return render(request, "gestionFacturas.html", {"facturas": facturas,"cajas": cajas})

def registrarFactura(request):
    NumFac=request.POST['txtnumFac']
    NombreFac=request.POST['txtnombreFac']
    Fecha=request.POST['dateFecha']
    Importe=request.POST['floatImporte']
    IdCaja=request.POST['txtidCaja']
    caja = Caja.objects.get(idCaja = IdCaja)

    facturas = Facturas.objects.create(numFac=NumFac, nombreFac=NombreFac, fecha=Fecha,importe=Importe,idCaja=caja)
    messages.success(request, 'Factura Registrada!')
    return redirect('/facturas')

def edicionFactura(request, numFac):
    facturas = Facturas.objects.get(numFac=numFac)
    cajas = Caja.objects.all()
    return render(request, "edicionFactura.html", {"facturas": facturas, "cajas": cajas})

def editarFactura(request):
    NumFac=request.POST['txtnumFac']
    NombreFac=request.POST['txtnombreFac']
    Fecha=request.POST['dateFecha']
    Importe=request.POST['floatImporte']
    IdCaja=request.POST['txtidCaja']
    caja = Caja.objects.get(idCaja = IdCaja)

    facturas = Facturas.objects.get(numFac=NumFac)
    facturas.numFac = NumFac
    facturas.nombreFac = NombreFac
    facturas.fecha = Fecha
    facturas.importe = Importe
    facturas.idCaja = caja
    facturas.save()

    messages.success(request, 'Factura Actualizada!')

    return redirect('/facturas')

def eliminarFactura(request, numFac):
    facturas = Facturas.objects.get(numFac=numFac)
    facturas.delete()

    messages.success(request, 'Factura Eliminada!')

    return redirect('/facturas')

def rutinas(request):
    rutinas = Rutinas.objects.all()
    cliente = Cliente.objects.all()
    entrenadores = Entrenador.objects.all()
    messages.success(request, 'Rutinas Listadas!')
    return render(request, "gestionRutinas.html", {"rutinas": rutinas,"cliente": cliente,"entrenadores": entrenadores})

def registrarRutina(request):
    IdRutina=request.POST['txtidRutina']
    Ejercicio=request.POST['txtEjercicio']
    Cantidad=request.POST['integerCantidad']
    Fecha=request.POST['dateFecha']
    IdCliente=request.POST['txtidCliente']
    cliente = Cliente.objects.get(idCliente = IdCliente)
    IdEntrenador=request.POST['txtidEntrenador']
    entrenadores = Entrenador.objects.get(idEntrenador = IdEntrenador)

    rutinas = Rutinas.objects.create(idRutina = IdRutina, ejercicio = Ejercicio, cantidad = Cantidad, fecha=Fecha, idCliente = cliente, idEntrenador = entrenadores)
    messages.success(request, 'Rutina Registrada!')
    return redirect('/rutinas')

def edicionRutina(request, idRutina):
    rutinas = Rutinas.objects.get(idRutina=idRutina)
    cliente = Cliente.objects.all()
    entrenadores = Entrenador.objects.all()
    return render(request, "edicionRutina.html", {"rutinas": rutinas,"cliente": cliente,"entrenadores": entrenadores})

def editarRutina(request):
    IdRutina=request.POST['txtidRutina']
    Ejercicio=request.POST['txtEjercicio']
    Cantidad=request.POST['integerCantidad']
    Fecha=request.POST['dateFecha']
    IdCliente=request.POST['txtidCliente']
    cliente = Cliente.objects.get(idCliente = IdCliente)
    IdEntrenador=request.POST['txtidEntrenador']
    entrenadores = Entrenador.objects.get(idEntrenador = IdEntrenador)

    rutinas = Rutinas.objects.get(idRutina=IdRutina)
    rutinas.idRutina = IdRutina
    rutinas.ejercicio = Ejercicio
    rutinas.cantidad = Cantidad
    rutinas.fecha = Fecha
    rutinas.idCliente = cliente
    rutinas.idEntrenador = entrenadores
    rutinas.save()

    messages.success(request, 'Rutina Actualizada!')

    return redirect('/rutinas')

def eliminarRutina(request, idRutina):
    rutinas = Rutinas.objects.get(idRutina=idRutina)
    rutinas.delete()

    messages.success(request, 'Rutina Eliminada!')

    return redirect('/rutinas')

def recibos(request):
    recibos = Recibos.objects.all()
    entrenadores = Entrenador.objects.all()
    messages.success(request, 'Recibos Listados!')
    return render(request, "gestionRecibos.html", {"recibos": recibos, "entrenadores": entrenadores})

def registrarRecibo(request):
    numRecibo=request.POST['txtnumRecibo']
    Sueldo=request.POST['floatSueldo']
    Fecha=request.POST['dateFecha']
    IdEntrenador=request.POST['txtidEntrenador']
    entrenadores = Entrenador.objects.get(idEntrenador = IdEntrenador)

    recibos = Recibos.objects.create(numRecibo = numRecibo, sueldo = Sueldo,  fecha=Fecha, idEntrenador = entrenadores)
    messages.success(request, 'Recibo Registrado!')
    return redirect('/recibos')

def edicionRecibo(request, numRecibo):
    recibos = Recibos.objects.get(numRecibo=numRecibo)
    entrenadores = Entrenador.objects.all()
    return render(request, "edicionRecibo.html", {"recibos": recibos,"entrenadores": entrenadores})


def editarRecibo(request):
    numRecibo=request.POST['txtnumRecibo']
    Sueldo=request.POST['floatSueldo']
    Fecha=request.POST['dateFecha']
    IdEntrenador=request.POST['txtidEntrenador']
    entrenadores = Entrenador.objects.get(idEntrenador = IdEntrenador)

    recibos = Recibos.objects.get(numRecibo=numRecibo)
    recibos.numRecibo = numRecibo
    recibos.sueldo = Sueldo
    recibos.fecha = Fecha
    recibos.idEntrenador = entrenadores
    recibos.save()

    messages.success(request, 'Recibo Actualizado!')

    return redirect('/recibos')


def eliminarRecibo(request, numRecibo):
    recibos = Recibos.objects.get(numRecibo=numRecibo)
    recibos.delete()

    messages.success(request, 'Recibo Eliminado!')

    return redirect('/recibos')

def registrarCliente(request):
    idCliente=request.POST['txtidCliente']
    Nombre=request.POST['txtNombre']
    Apellido=request.POST['txtApellido']

    cliente = Cliente.objects.create(idCliente=idCliente, nombre=Nombre, apellido=Apellido)
    messages.success(request, '¡Cliente Registrado!')
    return redirect('/')

def edicionCliente(request, idCliente):
    cliente = Cliente.objects.get(idCliente=idCliente)
    return render(request, "edicionCliente.html", {"cliente": cliente})

def editarCliente(request):
    idCliente=request.POST['txtidCliente']
    Nombre=request.POST['txtNombre']
    Apellido=request.POST['txtApellido']

    cliente = Cliente.objects.get(idCliente=idCliente)
    cliente.idCliente = idCliente
    cliente.nombre = Nombre
    cliente.apellido = Apellido
    cliente.save()

    messages.success(request, '¡Cliente Actualizado!')

    return redirect('/')


def eliminarCliente(request, idCliente):
    cliente = Cliente.objects.get(idCliente=idCliente)
    cliente.delete()

    messages.success(request, '¡Cliente Eliminado!')

    return redirect('/')

def clienteXclase(request):
    ClientexClase = clientesXclases.objects.all()
    clientes = Cliente.objects.all()
    clases = Clase.objects.all()
    messages.success(request, '¡ClientesXClases listados!')
    return render(request, "gestionClienteXClase.html", {"clienteXclase": ClientexClase,"clases": clases, "cliente": clientes})

def registrarClienteXClase(request):
    IdCxC=request.POST['txtidCxC']
    Fecha=request.POST['dateFecha']
    Estado=request.POST['txtEstado']
    IdCliente=request.POST['txtidCliente']
    cliente = Cliente.objects.get(idCliente = IdCliente)
    IdClase=request.POST['txtidClase']
    clases = Clase.objects.get(idClase = IdClase)
    

    clienteXclase = clientesXclases.objects.create( idCxC=IdCxC,fecha=Fecha, estado = Estado, idCliente = cliente,
                                                 idClase = clases)
    messages.success(request, 'clienteXclase Registrado!')
    return redirect('/clienteXclase')


def edicionClienteXClase(request, idCxC):
    clienteXclase = clientesXclases.objects.get(idCxC=idCxC)
    cliente = Cliente.objects.all()
    clases = Clase.objects.all()
    return render(request, "edicionClienteXClase.html", {"clienteXclase": clienteXclase,"cliente": cliente,"clases": clases})

def editarClienteXClase(request):
    IdCxC=request.POST['txtidCxC']
    Fecha=request.POST['dateFecha']
    Estado=request.POST['txtEstado']
    IdCliente=request.POST['txtidCliente']
    cliente = Cliente.objects.get(idCliente = IdCliente)
    IdClase=request.POST['txtidClase']
    clases = Clase.objects.get(idClase = IdClase)

    clienteXclase = clientesXclases.objects.get(idCxC=IdCxC)
    clienteXclase.idCxC = IdCxC
    clienteXclase.estado = Estado
    clienteXclase.fecha = Fecha
    clienteXclase.idCliente = cliente
    clienteXclase.idClase = clases
    clienteXclase.save()

    messages.success(request, 'cliente X clase Actualizado!')

    return redirect('/clienteXclase')

def eliminarClienteXClase(request, idCxC):
    clienteXclase = clientesXclases.objects.get(idCxC=idCxC)
    clienteXclase.delete()
    
    messages.success(request, 'ClienteXClase Eliminada!')

    return redirect('/clienteXclase')

def cobro(request):
    cobros = Cobro.objects.all()
    clientes = Cliente.objects.all()
    clases = Clase.objects.all()
    messages.success(request, '¡Cobros listados!')
    return render(request, "gestionCobro.html", {"cobros": cobros,"clases": clases, "cliente": clientes})


def registrarCobro(request):
    IdCobro=request.POST['txtidCobro']
    IdCliente=request.POST['txtidCliente']
    cliente = Cliente.objects.get(idCliente = IdCliente)
    IdClase=request.POST['txtidClase']
    clases = Clase.objects.get(idClase = IdClase)
    costoCuota=request.POST['floatCostoCuota']
    Fecha=request.POST['dateFecha']
    
    cobros = Cobro.objects.create( idCobro=IdCobro,  idCliente = cliente,
                                                 idClase = clases, CostoCuota = costoCuota,fecha=Fecha)
    messages.success(request, 'Cobro Registrado!')
    return redirect('/cobro')

def edicionCobro(request, idCobro):
    cobros = Cobro.objects.all(idCobro = idCobro)
    cliente = Cliente.objects.all()
    clases = Clase.objects.all()
    return render(request, "edicionCobro.html", {"cobros": cobros,"cliente": cliente,"clases": clases})

def editarCobro(request):
    IdCobro=request.POST['txtidCobro']
    IdCliente=request.POST['txtidCliente']
    cliente = Cliente.objects.get(idCliente = IdCliente)
    IdClase=request.POST['txtidClase']
    clases = Clase.objects.get(idClase = IdClase)
    costoCuota=request.POST['floatCostoCuota']
    Fecha=request.POST['dateFecha']
    
    cobros = Cobro.objects.get(idCobro=IdCobro)
    cobros.idCobro = IdCobro
    cobros.idCliente = cliente
    cobros.idClase = clases
    cobros.CostoCuota = costoCuota
    cobros.fecha = Fecha
    cobros.save()
    
    messages.success(request, 'cobro Actualizado!')

    return redirect('/cobro')

def informeAlumnoxclase(request):
    clientes = Cliente.objects.all()
    clases = Clase.objects.all()
    
    messages.success(request, 'AlumnoXclase listados!')
    return render(request, "gestionAlumnoXClase.html", {"clases": clases,"clientes": clientes})



 
 
 