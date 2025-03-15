package main

import (
	"fmt"
)

func main() {
	// Declaramos variables para almacenar los datos ingresados por el usuario
	var a, b, c string
	var d, e int

	// Solicitamos los nombres completos
	fmt.Print("Escriba sus nombres completos: ")
	fmt.Scanln(&a)

	// Solicitamos los apellidos completos
	fmt.Print("Escriba sus apellidos completos: ")
	fmt.Scanln(&b)

	// Solicitamos la profesión
	fmt.Print("Escriba su profesión: ")
	fmt.Scanln(&c)

	// Solicitamos el año de nacimiento
	fmt.Print("Escriba su año de nacimiento: ")
	fmt.Scan(&d)

	// Calculamos la edad restando el año de nacimiento al año actual (2025)
	e = 2025 - d

	// Mostramos el mensaje final con los datos ingresados
	fmt.Printf("El (La) %s %s %s tiene %d años\n", c, a, b, e)
}
