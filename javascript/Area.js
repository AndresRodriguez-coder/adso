function calcularArea(figura, var1, var2) {
    let pi = 3.1416;
    let res;

    switch (figura) {
        case "1": 
            res = (var1 * var2) / 2;
            console.log("El área del Rombo es: " + res);
            break;
        case "2":
            res = var1 * var2;
            console.log("El área del Rectángulo es: " + res);
            break;
        case "3": 
            res = var1 * var1; 
            console.log("El área del Cuadrado es: " + res);
            break;
        case "4": 
            res = ((var1 + var2) / 2) * var2; 
            console.log("El área del Trapecio es: " + res);
            break;
        default: 
            res = var1 * pi;
            console.log("Resultado: " + res);
    }
}

// Ejemplo de uso
calcularArea("1", 5, 10); 
calcularArea("2", 5, 10); 
calcularArea("3", 4, 0);   
calcularArea("4", 5, 10); 
calcularArea("5", 7, 0); 