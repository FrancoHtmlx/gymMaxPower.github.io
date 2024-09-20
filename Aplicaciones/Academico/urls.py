
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('registrarCliente/', views.registrarCliente),
    path('edicionCliente/<idCliente>', views.edicionCliente),
    path('editarCliente/', views.editarCliente),
    path('eliminarCliente/<idCliente>', views.eliminarCliente),
    path('entrenadores/', views.entrenadores),
    path('entrenadores/registrarEntrenador/', views.registrarEntrenador),
path('entrenadores/edicionEntrenador/<int:idEntrenador>/', views.edicionEntrenador, name='edicionEntrenador'),
    path('entrenadores/editarEntrenador/', views.editarEntrenador),
    path('entrenadores/eliminarEntrenador/<idEntrenador>', views.eliminarEntrenador),
    path('clases/', views.clases),
    path('clases/registrarClase/', views.registrarClase),
    path('clases/edicionClase/<idClase>', views.edicionClase),
    path('clases/editarClase/', views.editarClase),
    path('clases/eliminarClase/<idClase>', views.eliminarClase),
    path('cajas/', views.cajas),
    path('cajas/registrarCaja/', views.registrarCaja),
    path('cajas/edicionCaja/<idCaja>', views.edicionCaja),
    path('cajas/editarCaja/', views.editarCaja),
    path('cajas/eliminarCaja/<idCaja>', views.eliminarCaja),
    path('productos/', views.productos),
    path('productos/registrarProducto/', views.registrarProducto),
    path('productos/edicionProductos/<idProducto>', views.edicionProducto),
    path('productos/editarProducto/', views.editarProducto),
    path('productos/eliminarProducto/<idProducto>', views.eliminarProducto),
    path('facturas/', views.facturas),
    path('facturas/registrarFactura/', views.registrarFactura),
    path('facturas/edicionFactura/<numFac>', views.edicionFactura),
    path('facturas/editarFactura/', views.editarFactura),
    path('facturas/eliminarFactura/<numFac>', views.eliminarFactura),
    path('rutinas/', views.rutinas),
    path('rutinas/registrarRutina/', views.registrarRutina),
    path('rutinas/edicionRutina/<idRutina>', views.edicionRutina),
    path('rutinas/editarRutina/', views.editarRutina),
    path('rutinas/eliminarRutina/<idRutina>', views.eliminarRutina),
    path('recibos/', views.recibos),
    path('recibos/registrarRecibo/', views.registrarRecibo),
    path('recibos/edicionRecibo/<numRecibo>', views.edicionRecibo),
    path('recibos/editarRecibo/', views.editarRecibo),
    path('recibos/eliminarRecibo/<numRecibo>', views.eliminarRecibo),
    path('clienteXclase/', views.clienteXclase),
    path('clienteXclase/registrarClienteXClase/', views.registrarClienteXClase),
    path('clienteXclase/edicionClienteXClase/<idCxC>', views.edicionClienteXClase),
    path('clienteXclase/editarClienteXClase/', views.editarClienteXClase),
    path('clienteXclase/eliminarClienteXClase/<idCxC>', views.eliminarClienteXClase),
    path('informeAlumnoxclase/', views.informeAlumnoxclase),
    path('cobro/', views.cobro),
    path('cobro/registrarCobro/', views.registrarCobro),
    path('informeCobro/', views.informeCobro),
    
    
   
]
    
    


    
    


