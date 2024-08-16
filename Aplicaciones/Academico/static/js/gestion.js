<<<<<<< HEAD
(function () {
    console.log("hola")
    const btnEliminacion=document.querySelectorAll(".btnElminacion");

    btnEliminacion.forEach(btn => {
        console.log("entre1")
        btn.addEventListener('click', (e) => {
            console.log("entre2")
            const confirmacion = confirm('¿Seguro que desea eliminar el registro?');
            if(!confirmacion) {
                e.preventDefault();
            }
        });
    }); 
    
})();

=======
(function () {
    console.log("hola")
    const btnEliminacion=document.querySelectorAll(".btnElminacion");

    btnEliminacion.forEach(btn => {
        console.log("entre1")
        btn.addEventListener('click', (e) => {
            console.log("entre2")
            const confirmacion = confirm('¿Seguro que desea eliminar el registro?');
            if(!confirmacion) {
                e.preventDefault();
            }
        });
    }); 
    
})();

>>>>>>> 41072145d85b204857c4a4dbb8fdcbfd72693524
