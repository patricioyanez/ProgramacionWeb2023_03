function sumar()
{
    var n1 = document.getElementById("numero1").value;
    var n2 = document.getElementById("numero2").value;
    var total = parseInt(n1) + parseInt(n2);
    alert("El total es: " + total);
}

// Ejercicios: Agregar botones y funciones para realizar:
// resta, multiplicación y división.
function restar()
{
    var n1 = document.getElementById("numero1").value;
    var n2 = document.getElementById("numero2").value;
    var total = parseInt(n1) - parseInt(n2);
    alert("El total es: " + total);
}
function multiplicar()
{
    var n1 = document.getElementById("numero1").value;
    var n2 = document.getElementById("numero2").value;
    var total = parseInt(n1) * parseInt(n2);
    alert("El total es: " + total);
}
function dividir()
{
    var n1 = document.getElementById("numero1").value;
    var n2 = document.getElementById("numero2").value;
    
    n1 = parseInt(n1)
    n2 = parseInt(n2)
    if(n2 == 0)
    {
        alert("No se puede dividir por cero");
        return false;
    }
    var total = n1 / n2;
    alert("El total es: " + total);
}

// https://jquery.com/download/
