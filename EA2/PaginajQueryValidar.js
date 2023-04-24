$(function()
{
    // TODOS EL CODIGO JQUERY
    $('.divOcultar').hide(); // oculta el div

    $('.btnAceptar').click(function()
    {
        let nombre = $('.txtNombre').val(); // obtener el valor del input
        //alert("Hola " + nombre + ", ¿Cómo estás?");
        $('.txtNombre').val('');
        $('.txtResultado').val(nombre);
        $('.divOcultar').show(); // muestra el div
    })
})