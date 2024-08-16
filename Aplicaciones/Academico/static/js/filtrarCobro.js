function filtrarCobro(){
    var v = document.getElementById("txtidCliente").value;
    console.log(v)
    document.getElementById("idOculto").value = v;
    console.log(document.getElementById("idOculto").value );
        

}; 

function captura(idClase,costoCuota){
    console.log(idClase);
    console.log(costoCuota)
    
    document.getElementById("idOculto2").value = idClase;
    console.log(document.getElementById("idOculto2").value );

    document.getElementById("idOculto3").value = costoCuota;
    console.log(document.getElementById("idOculto3").value );  

}; 