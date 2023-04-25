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

// ejercicio: validar el rut.
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
        else if(!esValidoElRut($('.txtRut').val(),$('.txtDv').val()))
        {
            alert("El rut no es válido");
            $('.txtDv').focus();
        }
        else if(!$.trim($('.txtNombre').val()))
        {
            alert("Falta el nombre");
            $('.txtNombre').focus();
        }
        else if(!$('.txtEmail').val())
        {
            alert("Falta el email");
            $('.txtEmail').focus();
        }
        else if(!emailRegex.test($('.txtEmail').val()))
        { //verifica que el formato del correo este correcto
            alert("Formato de correo no es válido");
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

    function esValidoElRut(Rut,Digito)
    {
        Digito = Digito.toUpperCase();
		var longitud        = Rut.length;
		var factor          = 2;
		var sumaProducto    = 0;
		var con             = 0;
		var caracter     	= 0;
 
		for( con=longitud-1; con>=0; con--)
		{
			caracter = Rut.charAt(con);
			sumaProducto += (factor * caracter);
			if (++factor > 7)
				factor=2;		
		}
 
        var digitoAuxiliar	= 11-(sumaProducto % 11);   
        var caracteres		= "-123456789K0";
        var digitoCaracter= caracteres.charAt(digitoAuxiliar);
        return digitoCaracter == Digito ? 1 : 0;            
    }   
})