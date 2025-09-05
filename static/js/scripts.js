// Archivo: static/js/scripts.js

//  ostrar alerta de confirmación con animación
`document.querySelectorAll(".btn-danger").forEach(button => {
    button.addEventListener("click", function (event) {
        if (!confirm("¿Estás seguro de realizar esta acción?")) {
            event.preventDefault();
        }
    });
});`

// Animación de scroll al cargar
document.addEventListener("DOMContentLoaded", function () {
    document.body.style.opacity = "0";
    document.body.style.transition = "opacity 1s ease-in-out";
    document.body.style.opacity = "1";
});
