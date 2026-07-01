const botonSesion = document.getElementById("boton-sesion");
botonSesion.addEventListener("click", function () {
    alert("Bienvenido a la tienda de flores");
});
const enlaceEnviar = document.getElementById("enviar-flores");
enlaceEnviar.addEventListener("mouseenter", function () {
    enlaceEnviar.textContent = "Enviar bouquets";
});
enlaceEnviar.addEventListener("mouseleave", function () {
    enlaceEnviar.textContent = "Enviar flores";
});
const botonesComprar = document.querySelectorAll(".boton-comprar");
botonesComprar.forEach(function (boton) {
    boton.addEventListener("click", function () {
        boton.style.display = "none";
    });
});