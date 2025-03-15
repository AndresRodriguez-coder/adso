package main

import (
	"fmt"
)

func main() {
	// Lista de nombres
	names := []string{"Ana", "Pablo", "Diego", "Carmen"}

	// Lista de diccionarios (slice de mapas)
	people := []map[string]interface{}{
		{"nombre": "Ana", "edad": 28},
		{"nombre": "Pablo", "edad": 35},
		{"nombre": "Luis", "edad": 38},
	}

	// Imprimir nombre y edad de cada persona
	for _, person := range people {
		fmt.Println(person["nombre"])
		fmt.Println(person["edad"])
		fmt.Println(people) // Mostrar toda la lista
	}

	// Crear una nueva lista con solo los nombres
	var listaNames []string
	for _, person := range people {
		listaNames = append(listaNames, person["nombre"].(string))
	}
	fmt.Println(listaNames)

	// Lista de números
	numbers := []int{1, 2, 3, 4, 5}
	for i, number := range numbers {
		numbers[i] = number + 3
	}
	fmt.Println(numbers)
}
