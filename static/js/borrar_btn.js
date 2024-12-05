
const reset_form_busqueda = document.getElementById("reset_form_busqueda");
const form_filtro_productos = document.getElementById("form_filtro_productos");

reset_form_busqueda.addEventListener("click", (event) => {
    event.preventDefault();

    /*
    console.log("limpiando formulario")
    nombre.value = null;
    precio_min.value = null
    precio_max.value = null
    fecha_vencimiento_min.value = null
    fecha_vencimiento_max.value = null
    */

    let inputs = document.querySelectorAll('.input');

    inputs = [...inputs]

    for (const input of inputs) {
        input.value = null
    }

    form_filtro_productos.submit()
})

