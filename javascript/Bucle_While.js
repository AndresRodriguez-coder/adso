let contador = 0;
while (contador < 10) {
    contador += 1;
    console.log("Iteración", contador);
}

// Bucle infinito con break si no se cumple la condición
while (true) {
    let a = parseInt(prompt("Introduzca un valor mayor que 5:"));

    if (a > 5) {
        console.log("Es correcto");
    } else {
        console.log("Es incorrecto, pruebe de nuevo");
        break;
    }
}
