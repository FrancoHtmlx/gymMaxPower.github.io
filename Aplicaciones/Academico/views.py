
from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == 'POST':
        Nombre = request.POST['txtNombre']
        Apellido = request.POST['txtApellido']
        Telefono = request.POST['txtTelefono']
        Direccion = request.POST['txtDireccion']

        # Crear nuevo entrenador, el campo id es auto-generado
        entrenador = Entrenador(nombre=Nombre, apellido=Apellido,
                                telefono=Telefono, direccion=Direccion)
        entrenador.save()
        messages.success(request, 'Entrenador Registrado!')
        return redirect('/entrenadores')

    # Si no es POST, se redirige o se maneja de otra forma
    return redirect('/entrenadores')

@login_required
def edicionEntrenador(request, id):
    entrenador = get_object_or_404(Entrenador, pk=id)
    return render(request, "edicionEntrenador.html", {"entrenador": entrenador})

@login_required
def editarEntrenador(request):
    if request.method == 'POST':
        id = request.POST['txtId']
        Nombre = request.POST['txtNombre']
        Apellido = request.POST['txtApellido']
        Telefono = request.POST['txtTelefono']
        Direccion = request.POST['txtDireccion']

        entrenador = get_object_or_404(Entrenador, pk=id)
        entrenador.nombre = Nombre
        entrenador.apellido = Apellido
        entrenador.telefono = Telefono
        entrenador.direccion = Direccion
        entrenador.save()

        messages.success(request, 'Entrenador Actualizado!')
        return redirect('/entrenadores')

    # Si no es POST, se redirige o se maneja de otra forma
    return redirect('/entrenadores')

@login_required
def eliminarEntrenador(request, id):
    entrenador = get_object_or_404(Entrenador, pk=id)
    entrenador.delete()

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
    if request.method == 'POST':
        Nombre = request.POST['txtNombre']
        Dia = request.POST['txtDia']
        Horario = request.POST['txtHorario']
        Fecha = request.POST['dateFecha']
        CostoCuotas = request.POST['floatCostoCuotas']

        clase = Clase.objects.create(nombre=Nombre, dia=Dia,
        horario=Horario, fecha=Fecha, costoCuotas=CostoCuotas)
        messages.success(request, 'Clase Registrada!')
        return redirect('/clases')

    return render(request, "registrarClase.html")

@login_required
def edicionClase(request, id):
    clase = get_object_or_404(Clase, pk=id)
    return render(request, "edicionClase.html", {"clase": clase})

@login_required
def editarClase(request):
    if request.method == 'POST':
        id = request.POST['txtId']
        Nombre = request.POST['txtNombre']
        Dia = request.POST['txtDia']
        Horario = request.POST['txtHorario']
        Fecha = request.POST['dateFecha']
        CostoCuotas = request.POST['floatCostoCuotas']

        clase = get_object_or_404(Clase, pk=id)
        clase.nombre = Nombre
        clase.dia = Dia
        clase.horario = Horario
        clase.fecha = Fecha
        clase.costoCuotas = CostoCuotas
        clase.save()

        messages.success(request, 'Clase Actualizada!')
        return redirect('/clases')

    return render(request, "editarClase.html")

@login_required
def eliminarClase(request, id):
    clase = get_object_or_404(Clase, pk=id)
    clase.delete()

    messages.success(request, 'Clase Eliminada!')
    return redirect('/clases')

@login_required
def cajas(request):
    cajas = Caja.objects.all()
    messages.success(request, '¡Cajas Listadas!')
    return render(request, "gestionCaja.html", {"cajas": cajas})

@login_required
def registrarCaja(request):
    if request.method == 'POST':
        Tipo = request.POST['txtTipo']
        Monto = request.POST['floatMonto']
        Fecha = request.POST['dateFecha']

        caja = Caja.objects.create(tipo=Tipo, monto=Monto, fecha=Fecha)
        messages.success(request, 'Caja Registrada!')
        return redirect('/cajas')
    return render(request, "registrarCaja.html")

@login_required
def edicionCaja(request, idCaja):
    caja = get_object_or_404(Caja, pk=idCaja)
    return render(request, "edicionCaja.html", {"caja": caja})

@login_required
def editarCaja(request):
    if request.method == 'POST':
        idCaja = request.POST['txtidCaja']
        Tipo = request.POST['txtTipo']
        Monto = request.POST['floatMonto']
        Fecha = request.POST['dateFecha']

        caja = get_object_or_404(Caja, pk=idCaja)
        caja.tipo = Tipo
        caja.monto = Monto
        caja.fecha = Fecha
        caja.save()

        messages.success(request, 'Caja Actualizada!')
        return redirect('/cajas')
    return render(request, "editarCaja.html")

@login_required
def eliminarCaja(request, idCaja):
    caja = get_object_or_404(Caja, pk=idCaja)
    caja.delete()

    messages.success(request, 'Caja Eliminada!')
    return redirect('/cajas')


@login_required
def productos(request):
    productos = Productos.objects.all()
    messages.success(request, '¡Productos Listados!')
    return render(request, "gestionProductos.html", {"productos": productos})

@login_required
def registrarProducto(request):
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        stock = request.POST['txtStock']
        
        productos = Productos.objects.create(nombre=nombre, stock=stock)
        messages.success(request, 'Producto Registrado!')
        return redirect('/productos')
    else:
        return render(request, "registrarProducto.html")  # Suponiendo que tienes una plantilla para el formulario

@login_required
def edicionProducto(request, id):
    producto = get_object_or_404(Productos, pk=id)
    return render(request, "edicionProductos.html", {"producto": producto})

@login_required
def editarProducto(request):
    if request.method == 'POST':
        id_producto = request.POST['txtidProducto']
        nombre = request.POST['txtNombre']
        stock = request.POST['txtStock']
        
        producto = get_object_or_404(Productos, pk=id_producto)
        producto.nombre = nombre
        producto.stock = stock
        producto.save()

        messages.success(request, 'Producto Actualizado!')
        return redirect('/productos')
    else:
        return redirect('/productos')  # Redirige si no es un POST

@login_required
def eliminarProducto(request, id):
    producto = get_object_or_404(Productos, pk=id)
    producto.delete()
    messages.success(request, 'Producto Eliminado!')
    return redirect('/productos')

@login_required
def facturas(request):
    facturas = Facturas.objects.all()
    cajas = Caja.objects.all()
    messages.success(request, 'Facturas Listadas!')
    return render(request, "gestionFacturas.html", {"facturas": facturas, "cajas": cajas})

@login_required
def registrarFactura(request):
    if request.method == 'POST':
        num_fac = request.POST['txtnumFac']
        nombre_fac = request.POST['txtnombreFac']
        fecha = request.POST['dateFecha']
        importe = request.POST['floatImporte']
        id_caja = request.POST['txtidCaja']
        caja = get_object_or_404(Caja, pk=id_caja)

        facturas = Facturas.objects.create(numFac=num_fac, nombreFac=nombre_fac, fecha=fecha, importe=importe, idCaja=caja)
        messages.success(request, 'Factura Registrada!')
        return redirect('/facturas')
    else:
        return redirect('/facturas')  # Redirige si no es un POST

@login_required
def edicionFactura(request, numFac):
    factura = get_object_or_404(Facturas, numFac=numFac)
    cajas = Caja.objects.all()
    return render(request, "edicionFactura.html", {"factura": factura, "cajas": cajas})

@login_required
def editarFactura(request):
    if request.method == 'POST':
        num_fac = request.POST['txtnumFac']
        nombre_fac = request.POST['txtnombreFac']
        fecha = request.POST['dateFecha']
        importe = request.POST['floatImporte']
        id_caja = request.POST['txtidCaja']
        caja = get_object_or_404(Caja, pk=id_caja)

        factura = get_object_or_404(Facturas, numFac=num_fac)
        factura.nombreFac = nombre_fac
        factura.fecha = fecha
        factura.importe = importe
        factura.idCaja = caja
        factura.save()

        messages.success(request, 'Factura Actualizada!')
        return redirect('/facturas')
    else:
        return redirect('/facturas')  # Redirige si no es un POST

@login_required
def eliminarFactura(request, numFac):
    factura = get_object_or_404(Facturas, numFac=numFac)
    factura.delete()
    messages.success(request, 'Factura Eliminada!')
    return redirect('/facturas')

@login_required
def rutinas(request):
    rutinas = Rutinas.objects.all()
    clientes = Cliente.objects.all()
    entrenadores = Entrenador.objects.all()
    messages.success(request, 'Rutinas Listadas!')
    return render(request, "gestionRutinas.html", {"rutinas": rutinas, "clientes": clientes, "entrenadores": entrenadores})

@login_required
def registrarRutina(request):
    if request.method == 'POST':
        ejercicio = request.POST['txtEjercicio']
        cantidad = request.POST['integerCantidad']
        fecha = request.POST['dateFecha']
        id_cliente = request.POST['txtidCliente']
        cliente = get_object_or_404(Cliente, pk=id_cliente)
        id_entrenador = request.POST['txtidEntrenador']
        entrenador = get_object_or_404(Entrenador, pk=id_entrenador)

        rutinas = Rutinas.objects.create(ejercicio=ejercicio, cantidad=cantidad, fecha=fecha, idCliente=cliente, idEntrenador=entrenador)
        messages.success(request, 'Rutina Registrada!')
        return redirect('/rutinas')
    else:
        return redirect('/rutinas')  # Redirige si no es un POST

@login_required
def edicionRutina(request, idRutina):
    rutina = get_object_or_404(Rutinas, pk=idRutina)
    clientes = Cliente.objects.all()
    entrenadores = Entrenador.objects.all()
    return render(request, "edicionRutina.html", {"rutina": rutina, "clientes": clientes, "entrenadores": entrenadores})

@login_required
def editarRutina(request):
    if request.method == 'POST':
        id_rutina = request.POST['txtidRutina']
        ejercicio = request.POST['txtEjercicio']
        cantidad = request.POST['integerCantidad']
        fecha = request.POST['dateFecha']
        id_cliente = request.POST['txtidCliente']
        cliente = get_object_or_404(Cliente, pk=id_cliente)
        id_entrenador = request.POST['txtidEntrenador']
        entrenador = get_object_or_404(Entrenador, pk=id_entrenador)

        rutina = get_object_or_404(Rutinas, pk=id_rutina)
        rutina.ejercicio = ejercicio
        rutina.cantidad = cantidad
        rutina.fecha = fecha
        rutina.idCliente = cliente
        rutina.idEntrenador = entrenador
        rutina.save()

        messages.success(request, 'Rutina Actualizada!')
        return redirect('/rutinas')
    else:
        return redirect('/rutinas')  # Redirige si no es un POST

@login_required
def eliminarRutina(request, idRutina):
    rutina = get_object_or_404(Rutinas, pk=idRutina)
    rutina.delete()

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
    if request.method == 'POST':
        num_recibo = request.POST['txtnumRecibo']
        sueldo = request.POST['floatSueldo']
        fecha = request.POST['dateFecha']
        id_entrenador = request.POST['txtidEntrenador']
        entrenador = get_object_or_404(Entrenador, pk=id_entrenador)

        recibo = Recibos.objects.create(numRecibo=num_recibo, sueldo=sueldo, fecha=fecha, idEntrenador=entrenador)
        messages.success(request, 'Recibo Registrado!')
        return redirect('/recibos')
    else:
        return redirect('/recibos')  # Redirige si no es un POST

@login_required
def edicionRecibo(request, numRecibo):
    recibo = get_object_or_404(Recibos, numRecibo=numRecibo)
    entrenadores = Entrenador.objects.all()
    return render(request, "edicionRecibo.html", {"recibo": recibo, "entrenadores": entrenadores})

@login_required
def editarRecibo(request):
    if request.method == 'POST':
        num_recibo = request.POST['txtnumRecibo']
        sueldo = request.POST['floatSueldo']
        fecha = request.POST['dateFecha']
        id_entrenador = request.POST['txtidEntrenador']
        entrenador = get_object_or_404(Entrenador, pk=id_entrenador)

        recibo = get_object_or_404(Recibos, numRecibo=num_recibo)
        recibo.sueldo = sueldo
        recibo.fecha = fecha
        recibo.idEntrenador = entrenador
        recibo.save()

        messages.success(request, 'Recibo Actualizado!')
        return redirect('/recibos')
    else:
        return redirect('/recibos')  # Redirige si no es un POST

@login_required
def eliminarRecibo(request, numRecibo):
    recibo = get_object_or_404(Recibos, numRecibo=numRecibo)
    recibo.delete()

    messages.success(request, 'Recibo Eliminado!')
    return redirect('/recibos')

@login_required
def registrarCliente(request):
    if request.method == 'POST':
        Nombre = request.POST['txtNombre']
        Apellido = request.POST['txtApellido']

        cliente = Cliente.objects.create(nombre=Nombre, apellido=Apellido)
        messages.success(request, '¡Cliente Registrado!')
        return redirect('/')  # Redirige a la página principal o a donde corresponda

    return render(request, "registrarCliente.html")  # Asegúrate de tener una plantilla para el registro

@login_required
def edicionCliente(request, idCliente):
    cliente = get_object_or_404(Cliente, pk=idCliente)  # Usar pk para IDs automáticos
    return render(request, "edicionCliente.html", {"cliente": cliente})

@login_required
def editarCliente(request):
    if request.method == 'POST':
        idCliente = request.POST['txtidCliente']
        Nombre = request.POST['txtNombre']
        Apellido = request.POST['txtApellido']

        cliente = get_object_or_404(Cliente, pk=idCliente)  # Usar pk para IDs automáticos
        cliente.nombre = Nombre
        cliente.apellido = Apellido
        cliente.save()

        messages.success(request, '¡Cliente Actualizado!')
        return redirect('/')  # Redirige a la página principal o a donde corresponda

    return render(request, "editarCliente.html")  # Asegúrate de tener una plantilla para la edición

@login_required
def eliminarCliente(request, idCliente):
    cliente = get_object_or_404(Cliente, pk=idCliente)  # Usar pk para IDs automáticos
    cliente.delete()

    messages.success(request, '¡Cliente Eliminado!')
    return redirect('/')  # Redirige a la página principal o a donde corresponda

@login_required
def clienteXclase(request):
    clienteXclase_list = clientesXclases.objects.all()
    clientes = Cliente.objects.all()
    clases = Clase.objects.all()
    messages.success(request, '¡ClientesXClases listados!')
    return render(request, "gestionClienteXClase.html", {"clienteXclase": clienteXclase_list, "clases": clases, "cliente": clientes})

@login_required
def registrarClienteXClase(request):
    if request.method == 'POST':
        Fecha = request.POST['dateFecha']
        Estado = request.POST['txtEstado']
        IdCliente = request.POST['txtidCliente']
        cliente = get_object_or_404(Cliente, pk=IdCliente)
        IdClase = request.POST['txtidClase']
        clases = get_object_or_404(Clase, pk=IdClase)
        
        clienteXclase = clientesXclases.objects.create(fecha=Fecha, estado=Estado, idCliente=cliente, idClase=clases)
        messages.success(request, '¡ClienteXClase Registrado!')
        return redirect('/clienteXclase')

    # Si no es POST, redirige o muestra un error.
    return redirect('/clienteXclase')

@login_required
def edicionClienteXClase(request, idCxC):
    clienteXclase = get_object_or_404(clientesXclases, pk=idCxC)
    clientes = Cliente.objects.all()
    clases = Clase.objects.all()
    return render(request, "edicionClienteXClase.html", {"clienteXclase": clienteXclase, "cliente": clientes, "clases": clases})

@login_required
def editarClienteXClase(request):
    if request.method == 'POST':
        IdCxC = request.POST['txtidCxC']
        Fecha = request.POST['dateFecha']
        Estado = request.POST['txtEstado']
        IdCliente = request.POST['txtidCliente']
        cliente = get_object_or_404(Cliente, pk=IdCliente)
        IdClase = request.POST['txtidClase']
        clases = get_object_or_404(Clase, pk=IdClase)

        clienteXclase = get_object_or_404(clientesXclases, pk=IdCxC)
        clienteXclase.fecha = Fecha
        clienteXclase.estado = Estado
        clienteXclase.idCliente = cliente
        clienteXclase.idClase = clases
        clienteXclase.save()

        messages.success(request, '¡ClienteXClase Actualizado!')
        return redirect('/clienteXclase')

    # Si no es POST, redirige o muestra un error.
    return redirect('/clienteXclase')

@login_required
def eliminarClienteXClase(request, idCxC):
    clienteXclase = get_object_or_404(clientesXclases, pk=idCxC)
    clienteXclase.delete()

    messages.success(request, '¡ClienteXClase Eliminada!')
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
    if request.method == 'POST':
        IdCli = request.POST.get('idOculto', None)
        cliente = get_object_or_404(Cliente, idCliente=IdCli)
        
        Fecha = request.POST.get('dateFecha', None)
        
        idC = clientesXclases.objects.filter(estado='activo', idCliente=IdCli).values_list("idClase", flat=True).first()
        clase = get_object_or_404(Clase, idClase=idC)

        costoCuota = Clase.objects.filter(idClase=idC).values_list("costoCuotas", flat=True).first()

        nuevo_cobro = Cobro.objects.create(
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


