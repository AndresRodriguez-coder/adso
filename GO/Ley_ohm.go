package main

import (
	"fmt"
)

// Función para calcular el voltaje (V = I * R)
func voltaje() {
	var corriente, resistencia float64
	fmt.Print("Ingrese la corriente (I) en amperios: ")
	fmt.Scan(&corriente)
	fmt.Print("Ingrese la resistencia (R) en ohmios: ")
	fmt.Scan(&resistencia)
	fmt.Printf("El voltaje V es: %.2f V\n", corriente*resistencia)
}

// Función para calcular la corriente (I = V / R)
func corriente() {
	var voltaje, resistencia float64
	fmt.Print("Ingrese un voltaje en voltios: ")
	fmt.Scan(&voltaje)
	fmt.Print("Ingrese la resistencia en ohmios: ")
	fmt.Scan(&resistencia)
	fmt.Printf("La corriente I es: %.2f A\n", voltaje/resistencia)
}

// Función para calcular la resistencia (R = V / I)
func resistencia() {
	var voltaje, corriente float64
	fmt.Print("Ingrese el voltaje en voltios: ")
	fmt.Scan(&voltaje)
	fmt.Print("Ingrese la corriente I en amperios: ")
	fmt.Scan(&corriente)
	fmt.Printf("La resistencia R es: %.2f ohmios\n", voltaje/corriente)
}

func main() {
	var opcion int

	// Menú de opciones
	fmt.Println("=== Calculadora de la Ley de Ohm ===")
	fmt.Println("1. Calcular Voltaje")
	fmt.Println("2. Calcular Corriente")
	fmt.Println("3. Calcular Resistencia")
	fmt.Print("Seleccione una opción (1-3): ")
	fmt.Scan(&opcion)

	// Estructura switch para manejar la selección del usuario
	switch opcion {
	case 1:
		voltaje()
	case 2:
		corriente()
	case 3:
		resistencia()
	default:
		fmt.Println("Opción no válida.")
	}
}
