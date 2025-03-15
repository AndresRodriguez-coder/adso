package main

import (
	"fmt"
)

// Definimos una estructura para los barcos
type Barco struct {
	Nombre    string
	Tipo      string
	Color     string
	Año       int
	Matricula string
}

func main() {
	// Creamos un slice de estructuras Barco
	barcos := []Barco{
		{"Poseidón", "yate", "blanco", 2015, "BRC1234"},
		{"Nautilus", "submarino", "gris", 2008, "SUB5678"},
		{"Mistral", "velero", "azul", 2020, "VEL9012"},
		{"Leviatán", "buque de carga", "rojo", 2012, "CARG3456"},
	}

	// Modificamos el color del primer barco (Poseidón) a azul
	barcos[0].Color = "azul"

	// Imprimimos el primer barco modificado
	fmt.Println("Barco modificado:", barcos[0])

	// Iteramos sobre todos los barcos e imprimimos sus datos
	fmt.Println("\nLista de barcos:")
	for _, barco := range barcos {
		fmt.Println(barco)
	}
}
