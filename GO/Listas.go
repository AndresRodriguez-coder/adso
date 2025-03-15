package main

import (
	"fmt"
)

func main() {
	// Declaramos una lista de enteros (slice en Go)
	numeros := []int{10, 20, 30, 40, 50}

	// Agregar elementos al inicio y al final
	numeros = append([]int{5}, numeros...) // Agregar al inicio
	numeros = append(numeros, 60)          // Agregar al final

	// Imprimir la lista de números
	fmt.Println("Lista de números:")
	for _, num := range numeros {
		fmt.Print(num, " ")
	}
}
