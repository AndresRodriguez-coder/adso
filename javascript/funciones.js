function validarNumeros(a, b) {
    // Usamos una estructura condicional para comparar si "a" es igual a "b".
    if (a === b) {
        // Si son iguales, retornamos true.
        return true;
    } else {
        // Si no son iguales, retornamos false.
        return false;
    }
}

// Solicitamos al usuario que ingrese un número y lo convertimos a entero.
const a = parseInt(prompt("Introduzca un número"), 10);

// Solicitamos al usuario que ingrese otro número y lo convertimos a entero.
const b = parseInt(prompt("Introduzca otro número"), 10);

// Llamamos a la función "validarNumeros" pasando los dos números ingresados como argumentos y almacenamos el resultado en "resultado".
const resultado = validarNumeros(a, b);

// Usamos una estructura condicional para verificar el valor de "resultado".
if (resultado) {
    // Si "resultado" es true, imprimimos "Son iguales".
    console.log("Son iguales");
} else {
    // Si "resultado" es false, imprimimos "Son distintos".
    console.log("Son distintos");
}