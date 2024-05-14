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