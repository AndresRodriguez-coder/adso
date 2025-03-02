// Solicitar la operación al usuario
console.log("Seleccione la operación a realizar:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Potencia\n6. Raíz\n7. Suma de potencias\n8. Promedio\n9. Comparación entre A y B");
let operacion = prompt("Ingrese el número de la operación:");

// Solicitar los valores A y B
let A = parseFloat(prompt("Ingrese valor A:"));
let B = parseFloat(prompt("Ingrese valor B:"));

let res; // Variable para almacenar el resultado

switch (operacion) {
    case "1":
        res = A + B;
        console.log("La suma de los números es: " + res);
        break;
    case "2":
        res = A - B;
        console.log("La resta de los números es: " + res);
        break;
    case "3":
        res = A * B;
        console.log("La multiplicación de los números es: " + res);
        break;
    case "4":
        if (B !== 0) {
            res = A / B;
            console.log("La división de los números es: " + res);
        } else {
            console.log("Error: No se puede dividir por 0.");
        }
        break;
    case "5":
        res = Math.pow(A, B);
        console.log("La potencia es: " + res);
        break;
    case "6":
        if (B !== 0) {
            res = Math.pow(A, 1 / B);
            console.log("La raíz es: " + res);
        } else {
            console.log("Error: No se puede calcular la raíz con B = 0.");
        }
        break;
    case "7":
        res = Math.pow(A, B) + Math.pow(A, B);
        console.log("La suma de potencias es: " + res);
        break;
    case "8":
        res = (A + B) / 2;
        console.log("El promedio de los dos números es: " + res);
        break;
    case "9":
        if (A === B) {
            console.log("Los números son iguales: " + A);
        } else if (A > B) {
            console.log("El número mayor es: " + A);
        } else {
            console.log("El número mayor es: " + B);
        }
        break;
    default:
        console.log("Opción no válida. Intente de nuevo.");
}