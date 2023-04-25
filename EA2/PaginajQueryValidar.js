$(function()
{
    let numero = '1234567890';
    let letras = ' qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNMáéíóúÁÉÍÓÚ';

    // expresión regular
    let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,4})+$/

// TAREA: validar dv, nombre y correo
    $('.txtRut').keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numero.indexOf(caracter) < 0)
            return false;
    })
    $('.txtDv').keypress(function(e)
    {
        let patron = numero + 'kK';
        let caracter = String.fromCharCode(e.which);
        if(patron.indexOf(caracter) < 0)
            return false;
    })
    $('.txtNombre').keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;
    })
    $('.txtEmail').keypress(function(e)
    {
        let patron = numero + 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@_-.';
        let caracter = String.fromCharCode(e.which);
        if(patron.indexOf(caracter) < 0)
            return false;
    })


    $('.btnAceptar').click(function()
    {
        if(!$('.txtRut').val())
        {
            alert("Falta el rut");
            $('.txtRut').focus();
        }
        else if(!$('.txtDv').val())
        {
            alert("Falta el dv");
            $('.txtDv').focus();
        }
        else if(!$('.txtNombre').val())
        {
            alert("Falta el nombre");
            $('.txtNombre').focus();
        }
        else if(!$('.txtEmail').val())
        {
            alert("Falta el email");
            $('.txtEmail').focus();
        }
    })
    $('.btnLimpiar').click(function()
    {
        $('.txtRut, .txtDv, .txtNombre, .txtEmail').val('');
        /*$('.txtRut').val('');
        $('.txtDv').val('');
        $('.txtNombre').val('');
        $('.txtEmail').val('');*/
        $('.txtRut').focus();
    })
})