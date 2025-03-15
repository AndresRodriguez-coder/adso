package main

import (
	"fmt"
)

func main() {
	var figura string
	pi := 3.1416

	// Solicitar al usuario la figura a calcular
	fmt.Print("Seleccione la figura a calcular, 1 para Rombo, 2 para Rectángulo, 3 para Cuadrado, 4 para Trapecio: ")
	fmt.Scan(&figura)

	// Solicitar valores al usuario
	var var1, var2 int
	fmt.Print("Ingrese el primer valor: ")
	fmt.Scan(&var1)
	fmt.Print("Ingrese el segundo valor: ")
	fmt.Scan(&var2)

	var res float64 // Variable para almacenar el resultado

	// Estructura switch en lugar de match-case
	switch figura {
	case "1":
		res = float64(var1*var2) / 2
		fmt.Println("El Área del Rombo es:", res)
	case "2":
		res = float64(var1 * var2)
		fmt.Println("El Área del Rectángulo es:", res)
	case "3":
		res = float64(var1 * var2)
		fmt.Println("El Área del Cuadrado es:", res)
	case "4":
		res = float64(var1 * var2)
		fmt.Println("El Área del Trapecio es:", res)
	default:
		res = float64(var1) * pi
		fmt.Println("Resultado usando pi:", res)
	}
}
