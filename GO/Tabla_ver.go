package main

import "fmt"

func main() {
	// Declaración de variables booleanas
	a := true
	b := false

	// Operación lógica AND (&&) entre 'a' y 'b'
	fmt.Println(a && b) // false (0)

	// Declaración de variables enteras
	aNum, bNum, c, d := 2, 3, 4, 10

	// Evaluación de condiciones lógicas
	fmt.Println(aNum == bNum && c < d)    // false (0)
	fmt.Println(!(aNum == bNum) && c < d) // true (1)
}
