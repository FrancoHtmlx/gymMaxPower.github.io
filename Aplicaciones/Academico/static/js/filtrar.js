<<<<<<< HEAD
function filtrar(){
    var v = document.getElementById("select_id").value;
    console.log(v)
    document.getElementById("idOculto").value = v;
    console.log(document.getElementById("idOculto").value )
    //activos = ClientexClase = clientesXclases.objects.filter(estado = 'activo',idClase= v).values_list("idCliente");
    //clientes = Cliente.objects.filter(idCliente_id__in=activos)
        

}; 

=======
(function filtrar(){
    const informe = document.querySelector('#informe');
    console.log(informe)
        informe.addEventListener('change', () => {
            let valorOption = informe.value;
            console.log(valorOption);

            var optionSelect= informe.options[informe.SelectedIndex].value;

            lista = ClientexClase = clientesXclases.objects.filter(estado = 'activo',idClase_id=optionSelect.value).values_list("idCliente_id");
            clientes = Cliente.objects.filter(idCliente__in=lista)

            

        });

        

})();
>>>>>>> 41072145d85b204857c4a4dbb8fdcbfd72693524
