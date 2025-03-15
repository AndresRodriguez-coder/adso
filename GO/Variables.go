package main

import (
	"fmt"
	"math"
)

func main() {
	// Declaración de variables
	a, b := 10, 4

	// Multiplicación
	fmt.Println("La primera variable es:", a)
	fmt.Println("El signo de la operación es: * ")
	fmt.Println("La segunda variable es:", b)
	c := a * b
	fmt.Println("El resultado es:", c)
	fmt.Println("Tipo de dato: int")

	// División
	fmt.Println("\nLa primera variable es:", a)
	fmt.Println("El signo de la operación es: / ")
	fmt.Println("La segunda variable es:", b)
	d := float64(a) / float64(b) // Conversión a float64 para precisión
	fmt.Println("El resultado es:", d)
	fmt.Println("Tipo de dato: float64")

	// Suma
	fmt.Println("\nLa primera variable es:", a)
	fmt.Println("El signo de la operación es: + ")
	fmt.Println("La segunda variable es:", b)
	c = a + b
	fmt.Println("El resultado es:", c)
	fmt.Println("Tipo de dato: int")

	// Resta
	fmt.Println("\nLa primera variable es:", a)
	fmt.Println("El signo de la operación es: - ")
	fmt.Println("La segunda variable es:", b)
	c = a - b
	fmt.Println("El resultado es:", c)
	fmt.Println("Tipo de dato: int")

	// Potencia
	fmt.Println("\nLa primera variable es:", a)
	fmt.Println("El signo de la operación es: ** (en Go se usa math.Pow)")
	fmt.Println("La segunda variable es:", b)
	e := math.Pow(float64(a), float64(b)) // Uso de math.Pow para la potencia
	fmt.Println("El resultado es:", e)
	fmt.Println("Tipo de dato: float64")

	// Módulo
	fmt.Println("\nLa primera variable es:", a)
	fmt.Println("El signo de la operación es: % ")
	fmt.Println("La segunda variable es:", b)
	c = a % b
	fmt.Println("El resultado es:", c)
	fmt.Println("Tipo de dato: int")
}
