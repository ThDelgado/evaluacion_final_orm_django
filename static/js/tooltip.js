var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})
/*
pegar donde va tooltip


{% block recursos_js %} 
    {% load static %}
    <script src="{% static "js/tooltip.js" %}"></script>

{% endblock %}

TOOLTIP SENCILLO
-------------------
<a href="{% url "detalle_post" post.id %}"
    data-bs-toggle="tooltip" 
    data-bs-placement="right" 
    data-bs-title="Clic para ver detalle del curso: {{post.titulo}}"
    data-bs-custom-class="custom-tooltip"
    >
    <img src="{{post.imagen}}" alt="{{post.titulo}}" class="img-table">
</a>


*/

/* 
ejemplo tooltip en html
----------------------------
    <a href="" class="mx-2"
        data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Actualizar"
        data-bs-custom-class="custom-actualizar">
        <i class="fa-solid fa-pen-to-square text-warning"></i>
    </a>
        <a href="{% url "eliminar_comentario" comentario.id %}" class="mx-2"
            data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Eliminar"
            data-bs-custom-class="custom-eliminar">
            <i class="fa-regular fa-trash-can text-danger"></i>
    </a>

    EN CSS
    ------------
    tooltips stilos 
    
    .custom - actualizar {
     --bs - tooltip - bg: var(--bs - warning);

    }

    .custom - eliminar {
    --bs - tooltip - bg: var(--bs - danger);
    --bs - tooltip - color: var(--bs - white);

    }

*/