package main

import (
	"fmt"
)

func main() {
	// Declaración de una variable entera
	a := 2

	// Estructura condicional if-else
	if a == 2 {
		fmt.Println("a vale 2")
	} else {
		fmt.Println("a es distinto de 2")
	}

	// Declaración de variables de diferentes tipos
	nombre := "Ana"
	edad := 28
	ciudad := "Colombia"

	// Uso de operadores lógicos (and: &&, or: ||, not: !)
	if nombre == "Ana" && edad == 28 && ciudad == "Colombia" {
		fmt.Println("Su nombre es Ana, tiene 28 años y es de Colombia")
	} else if nombre == "Ana" && edad != 28 {
		fmt.Println("Su nombre es Ana y no tiene 28 años")
	} else if nombre != "Ana" && edad == 28 {
		fmt.Println("Su nombre no es Ana y tiene 28 años")
	} else {
		fmt.Println("No se llama Ana ni tiene 28 años")
	}
}
