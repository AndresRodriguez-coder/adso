package main

import (
	"fmt"
)

// Función que valida si dos números son iguales
func validarNumeros(a, b int) bool {
	// Compara si a es igual a b y devuelve true o false
	return a == b
}

func main() {
	// Declaramos variables para almacenar los números
	var a, b int

	// Solicitamos al usuario que ingrese el primer número
	fmt.Print("Introduzca un número: ")
	fmt.Scan(&a)

	// Solicitamos al usuario que ingrese el segundo número
	fmt.Print("Introduzca otro número: ")
	fmt.Scan(&b)

	// Llamamos a la función validarNumeros y almacenamos el resultado
	resultado := validarNumeros(a, b)

	// Evaluamos el resultado y mostramos el mensaje correspondiente
	if resultado {
		fmt.Println("Son iguales")
	} else {
		fmt.Println("Son distintos")
	}
}
