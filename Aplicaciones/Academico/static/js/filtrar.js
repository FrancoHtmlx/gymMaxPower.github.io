
function filtrar(){
    var v = document.getElementById("select_id").value;
    console.log(v)
    document.getElementById("idOculto").value = v;
    console.log(document.getElementById("idOculto").value )
    //activos = ClientexClase = clientesXclases.objects.filter(estado = 'activo',idClase= v).values_list("idCliente");
    //clientes = Cliente.objects.filter(idCliente_id__in=activos)
        

}; 




