package main

import (
	"fmt"
	"math"
)

func main() {
	var operacion int
	var A, B, res float64

	// Mostrar opciones al usuario
	fmt.Println("Seleccione operación a realizar:")
	fmt.Println("1. Suma")
	fmt.Println("2. Resta")
	fmt.Println("3. Multiplicación")
	fmt.Println("4. División")
	fmt.Println("5. Potencia")
	fmt.Println("6. Raíz")
	fmt.Println("7. Suma de potencias")
	fmt.Println("8. Promedio")
	fmt.Println("9. Comparación")
	fmt.Print("Opción: ")
	fmt.Scan(&operacion)

	// Pedir valores al usuario
	fmt.Print("Ingrese el primer valor: ")
	fmt.Scan(&A)
	fmt.Print("Ingrese el segundo valor: ")
	fmt.Scan(&B)

	// Estructura de control switch para seleccionar la operación
	switch operacion {
	case 1:
		res = A + B
		fmt.Println("La suma de los números es:", res)
	case 2:
		res = A - B
		fmt.Println("La resta de los números es:", res)
	case 3:
		res = A * B
		fmt.Println("La multiplicación de los números es:", res)
	case 4:
		if B != 0 {
			res = A / B
			fmt.Println("La división de los números es:", res)
		} else {
			fmt.Println("Error: División por cero no permitida.")
		}
	case 5:
		res = math.Pow(A, B)
		fmt.Println("La potencia es:", res)
	case 6:
		if B != 0 {
			res = math.Pow(A, 1.0/B)
			fmt.Println("La raíz es:", res)
		} else {
			fmt.Println("Error: No se puede calcular la raíz con exponente 0.")
		}
	case 7:
		res = math.Pow(A, B) + math.Pow(A, B)
		fmt.Println("La suma de potencias es:", res)
	case 8:
		res = (A + B) / 2
		fmt.Println("El promedio de los dos números es:", res)
	case 9:
		if A == B {
			fmt.Println("Los números son iguales:", A)
		} else if A > B {
			fmt.Println("El número mayor es:", A)
		} else {
			fmt.Println("El número mayor es:", B)
		}
	default:
		fmt.Println("Opción no válida. Intente de nuevo.")
	}
}
