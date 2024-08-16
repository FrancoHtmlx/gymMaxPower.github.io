from django.shortcuts import render, redirect
from .models import Cliente,Entrenador,Clase,Caja,Productos,Facturas,Rutinas,Recibos,clientesXclases,Cobro,alumnoXclase
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    cliente = Cliente.objects.all()
    messages.success(request, '¡Clientes Listados!')
    return render(request, "gestionCliente.html", {"cliente": cliente})
#minuto 55:44 min del video hoy miercoles 14 agosto.
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
                login(request, user)
                return redirect('signin')  # Redirige a la página de inicio de sesión
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El nombre de usuario ya existe. Por favor elige otro.'  # Mensaje de error
                })
            
        return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coinciden. Por favor, intenta de nuevo.'  # Mensaje de error
                
        })

       
def signout (request):
    logout(request)
    return redirect('signin')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
        'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',{
            'form': AuthenticationForm,
            'error': 'Username or Password is incorrect'
            })
        else:
            login(request, user)
            return redirect('/')
   
@login_required
def entrenadores(request):
    entrenadores = Entrenador.objects.all()
    messages.success(request, '¡Entrenadores Listados!')
    return render(request, "gestionEntrenador.html", {"entrenadores": entrenadores})

@login_required
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

@login_required
def edicionEntrenador(request, idEntrenador):
    entrenadores = Entrenador.objects.get(idEntrenador=idEntrenador)
    return render(request, "edicionEntrenador.html", {"entrenadores": entrenadores})

@login_required
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

@login_required
def eliminarEntrenador(request, idEntrenador):
    entrenadores = Entrenador.objects.get(idEntrenador=idEntrenador)
    entrenadores.delete()

    messages.success(request, 'Entrenador Eliminado!')

    return redirect('/entrenadores')

#clases = Clase.objects.filter(estado='activo')

@login_required
def clases(request):
    clases = Clase.objects.all()
    messages.success(request, '¡Clases Listados!')
    return render(request, "gestionClase.html", {"clases": clases})

@login_required
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

@login_required
def edicionClase(request, idClase):
    clases = Clase.objects.get(idClase=idClase)
    return render(request, "edicionClase.html", {"clases": clases})

@login_required
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

@login_required
def eliminarClase(request, idClase):
    clases = Clase.objects.get(idClase=idClase)
    clases.delete()

    messages.success(request, 'Clase Eliminada!')

    return redirect('/clases')

@login_required
def cajas(request):
    cajas = Caja.objects.all()
    messages.success(request, '¡Caja Listadas!')
    return render(request, "gestionCaja.html", {"cajas": cajas})

@login_required
def registrarCaja(request):
    idCaja=request.POST['txtidCaja']
    Tipo=request.POST['txtTipo']
    Monto=request.POST['floatMonto']
    Fecha=request.POST['dateFecha']

    caja = Caja.objects.create(idCaja=idCaja, tipo=Tipo, monto=Monto,
    fecha=Fecha)
    messages.success(request, 'Caja Registrada!')
    return redirect('/cajas')

@login_required
def edicionCaja(request, idCaja):
    cajas = Caja.objects.get(idCaja=idCaja)
    return render(request, "edicionCaja.html", {"cajas": cajas})

@login_required
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

@login_required
def eliminarCaja(request, idCaja):
    cajas = Caja.objects.get(idCaja=idCaja)
    cajas.delete()

    messages.success(request, 'Caja Eliminada!')

    return redirect('/cajas')

@login_required
def productos(request):
    productos = Productos.objects.all()
    messages.success(request, '¡Productos Listados!')
    return render(request, "gestionProductos.html", {"productos": productos})

@login_required
def registrarProducto(request):
    idProducto=request.POST['txtidProducto']
    Nombre=request.POST['txtNombre']
    Stock=request.POST['txtStock']

    productos = Productos.objects.create(idProducto=idProducto, nombre=Nombre, stock=Stock)
    messages.success(request, 'Producto Registrado!')
    return redirect('/productos')

@login_required
def edicionProducto(request, idProducto):
    productos = Productos.objects.get(idProducto=idProducto)
    return render(request, "edicionProductos.html", {"productos": productos})

@login_required
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

@login_required
def eliminarProducto(request, idProducto):
    productos = Productos.objects.get(idProducto=idProducto)
    productos.delete()

    messages.success(request, 'Producto Eliminado!')

    return redirect('/productos')

@login_required
def facturas(request):
    facturas = Facturas.objects.all()
    #print(str(facturas))
    cajas = Caja.objects.all()
    messages.success(request, 'Facturas Listadas!')
    return render(request, "gestionFacturas.html", {"facturas": facturas,"cajas": cajas})

@login_required
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

@login_required
def edicionFactura(request, numFac):
    facturas = Facturas.objects.get(numFac=numFac)
    cajas = Caja.objects.all()
    return render(request, "edicionFactura.html", {"facturas": facturas, "cajas": cajas})

@login_required
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

@login_required
def eliminarFactura(request, numFac):
    facturas = Facturas.objects.get(numFac=numFac)
    facturas.delete()

    messages.success(request, 'Factura Eliminada!')

    return redirect('/facturas')

@login_required
def rutinas(request):
    rutinas = Rutinas.objects.all()
    cliente = Cliente.objects.all()
    entrenadores = Entrenador.objects.all()
    messages.success(request, 'Rutinas Listadas!')
    return render(request, "gestionRutinas.html", {"rutinas": rutinas,"cliente": cliente,"entrenadores": entrenadores})

@login_required
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

@login_required
def edicionRutina(request, idRutina):
    rutinas = Rutinas.objects.get(idRutina=idRutina)
    cliente = Cliente.objects.all()
    entrenadores = Entrenador.objects.all()
    return render(request, "edicionRutina.html", {"rutinas": rutinas,"cliente": cliente,"entrenadores": entrenadores})

@login_required
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

@login_required
def eliminarRutina(request, idRutina):
    rutinas = Rutinas.objects.get(idRutina=idRutina)
    rutinas.delete()

    messages.success(request, 'Rutina Eliminada!')

    return redirect('/rutinas')

@login_required
def recibos(request):
    recibos = Recibos.objects.all()
    entrenadores = Entrenador.objects.all()
    messages.success(request, 'Recibos Listados!')
    return render(request, "gestionRecibos.html", {"recibos": recibos, "entrenadores": entrenadores})

@login_required
def registrarRecibo(request):
    numRecibo=request.POST['txtnumRecibo']
    Sueldo=request.POST['floatSueldo']
    Fecha=request.POST['dateFecha']
    IdEntrenador=request.POST['txtidEntrenador']
    entrenadores = Entrenador.objects.get(idEntrenador = IdEntrenador)

    recibos = Recibos.objects.create(numRecibo = numRecibo, sueldo = Sueldo,  fecha=Fecha, idEntrenador = entrenadores)
    messages.success(request, 'Recibo Registrado!')
    return redirect('/recibos')

@login_required
def edicionRecibo(request, numRecibo):
    recibos = Recibos.objects.get(numRecibo=numRecibo)
    entrenadores = Entrenador.objects.all()
    return render(request, "edicionRecibo.html", {"recibos": recibos,"entrenadores": entrenadores})

@login_required
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

@login_required
def eliminarRecibo(request, numRecibo):
    recibos = Recibos.objects.get(numRecibo=numRecibo)
    recibos.delete()

    messages.success(request, 'Recibo Eliminado!')

    return redirect('/recibos')

@login_required
def registrarCliente(request):
    idCliente=request.POST['txtidCliente']
    Nombre=request.POST['txtNombre']
    Apellido=request.POST['txtApellido']

    cliente = Cliente.objects.create(idCliente=idCliente, nombre=Nombre, apellido=Apellido)
    messages.success(request, '¡Cliente Registrado!')
    return redirect('/')

@login_required
def edicionCliente(request, idCliente):
    cliente = Cliente.objects.get(idCliente=idCliente)
    return render(request, "edicionCliente.html", {"cliente": cliente})

@login_required
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

@login_required
def eliminarCliente(request, idCliente):
    cliente = Cliente.objects.get(idCliente=idCliente)
    cliente.delete()

    messages.success(request, '¡Cliente Eliminado!')

    return redirect('/')

@login_required
def clienteXclase(request):
    ClientexClase = clientesXclases.objects.all()
    clientes = Cliente.objects.all()
    clases = Clase.objects.all()
    messages.success(request, '¡ClientesXClases listados!')
    return render(request, "gestionClienteXClase.html", {"clienteXclase": ClientexClase,"clases": clases, "cliente": clientes})

@login_required
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

@login_required
def edicionClienteXClase(request, idCxC):
    clienteXclase = clientesXclases.objects.get(idCxC=idCxC)
    cliente = Cliente.objects.all()
    clases = Clase.objects.all()
    return render(request, "edicionClienteXClase.html", {"clienteXclase": clienteXclase,"cliente": cliente,"clases": clases})

@login_required
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

@login_required
def eliminarClienteXClase(request, idCxC):
    clienteXclase = clientesXclases.objects.get(idCxC=idCxC)
    clienteXclase.delete()
    
    messages.success(request, 'ClienteXClase Eliminada!')

    return redirect('/clienteXclase')

@login_required
def cobro(request):
    cobros = Cobro.objects.all()
    clientes = Cliente.objects.all()
    clases = Clase.objects.all()
    messages.success(request, '¡Cobros listados!')
    return render(request, "gestionCobro.html", {"cobros": cobros,"clases": clases, "cliente": clientes})

@login_required
def registrarCobro(request):
    print("entra")
    # Obtener el idCobro del formulario
    IdCobro = request.POST.get('txtidCobro', None)
    
    # Verificar si el campo 'txtidCobro' se obtuvo
    if IdCobro is None:
        messages.error(request, 'El campo idCobro es requerido.')
        return redirect('/cobro')  # Redirige en caso de error
    
    # Obtener el idCliente del campo oculto
    IdCli = request.POST.get('idOculto', None)
    print(IdCli)
    cliente = Cliente.objects.filter(idCliente=IdCli)[0]
    
    if IdCli is None:
        messages.error(request, 'El campo idCliente es requerido.')
        return redirect('/cobro')  # Redirige en caso de error

    # Obtener la fecha del formulario
    Fecha = request.POST.get('dateFecha', None)
    
    if Fecha is None:
        messages.error(request, 'El campo Fecha es requerido.')
        return redirect('/cobro')  # Redirige en caso de error

    # Buscar el idClase correspondiente al idCliente
    idC = clientesXclases.objects.filter(estado='activo', idCliente=IdCli).values_list("idClase", flat=True).first()
    print(idC)
    clase=Clase.objects.filter(idClase=idC)[0]
    
    if idC is None:
        messages.error(request, 'No se encontró una clase activa para el cliente.')
        return redirect('/cobro')  # Redirige en caso de error

    # Obtener el costo de la cuota para la clase
    costoCuota = Clase.objects.filter(idClase=idC).values_list("costoCuotas", flat=True).first()
    print(costoCuota)
    
    if costoCuota is None:
        messages.error(request, 'No se encontró el costo de la cuota para la clase.')
        return redirect('/cobro')  # Redirige en caso de error

    # Crear el nuevo registro de cobro
    nuevo_cobro = Cobro.objects.create(
        idCobro=IdCobro,
        idCliente=cliente,
        idClase=clase,
        fecha=Fecha,
        CostoCuota=costoCuota
    )

    messages.success(request, 'Cobro registrado exitosamente!')
    return redirect('/cobro')

@login_required
def informeCobro(request):
    print("entre")

    # Obtener la fecha del formulario
    Fecha1 = request.POST.get('desde', None)
    print(Fecha1)
    
    #if Fecha1 is None:
        #messages.error(request, 'El campo Fecha es requerido.')
        #return redirect('/informeCobro')  # Redirige en caso de error
    
    # Obtener la fecha del formulario
    Fecha2 = request.POST.get('hasta', None)
    print(Fecha2)
    
    #if Fecha2 is None:
        #.error(request, 'El campo Fecha es requerido.')
        #return redirect('/informeCobro')  # Redirige en caso de error
    
    if Fecha1!=None and Fecha2!=None:
        print("entra al if")
        cobros = Cobro.objects.filter(fecha__gte=Fecha1,fecha__lte=Fecha2)
        return render(request, "informeCobro.html", {"cobros": cobros})
    else:
        return render(request, "informeCobro.html")

            
@login_required       
def informeAlumnoxclase(request):
    clientes = Cliente.objects.all()
    clases = Clase.objects.all()
    ClientexClase = clientesXclases.objects.all()
    
    #IdClas=request.POST['idOculto']
    
    IdClas = request.POST.get('idOculto', None)
    
    #clases = Clase.objects.get(idClase=IdClas)
    #print(IdClas)
    lista = ClientexClase = clientesXclases.objects.filter(estado = 'activo',idClase=IdClas).values_list("idCliente")
    clientes = Cliente.objects.filter(idCliente__in=lista)
    
    messages.success(request, 'AlumnoXclase listado!')
    return render(request, "gestionAlumnoXClase.html", {"clases": clases,"clientes": clientes,"ClienteXClase": ClientexClase})


