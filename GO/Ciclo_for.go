package main

import (
	"fmt"
	"math"
)

func main() {
	for {
		// Solicitar el primer valor
		fmt.Print("Ingrese el primer valor: ")
		var A int
		fmt.Scan(&A)

		// Solicitar el segundo valor
		fmt.Print("Ingrese el segundo valor: ")
		var C int
		fmt.Scan(&C)

		// Calcular la potencia
		valor := math.Pow(float64(A), float64(C))

		// Mostrar el resultado
		fmt.Println("La potencia de", A, "sobre", C, "es:", valor)

		// Preguntar si desea continuar
		var opcion string
		fmt.Print("¿Desea calcular otra potencia? (s/n): ")
		fmt.Scan(&opcion)
		if opcion != "s" {
			break
		}
	}
}
