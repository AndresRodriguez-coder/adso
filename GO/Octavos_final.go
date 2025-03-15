package main

import (
	"fmt"
)

func jugarMundial(equipos []string) {
	fases := []string{"Octavos de final", "Cuartos de final", "Semifinal", "Final"}

	var tercerLugar string
	for len(equipos) > 1 {
		fase := fases[0]
		fases = fases[1:] // Eliminar la fase actual

		fmt.Println("\n", fase)

		var ganadores []string
		for i := 0; i < len(equipos); i += 2 {
			equipo1 := equipos[i]
			equipo2 := equipos[i+1]

			var goles1, goles2 int
			for {
				fmt.Printf("Goles de %s: ", equipo1)
				_, err1 := fmt.Scan(&goles1)
				fmt.Printf("Goles de %s: ", equipo2)
				_, err2 := fmt.Scan(&goles2)

				// Validación de entrada
				if err1 != nil || err2 != nil {
					fmt.Println("Entrada inválida. Intente de nuevo.")
					continue
				}

				// Evitar empate
				if goles1 == goles2 {
					fmt.Println("No se permiten empates. Introduzca un nuevo marcador.")
					continue
				}
				break
			}

			// Determinar ganador
			if goles1 > goles2 {
				ganadores = append(ganadores, equipo1)
			} else {
				ganadores = append(ganadores, equipo2)
			}

			// Guardar el equipo que perdió en la semifinal para el tercer lugar
			if len(equipos) == 4 {
				tercerLugar = equipo1
				if goles1 > goles2 {
					tercerLugar = equipo2
				}
			}
		}

		equipos = ganadores
	}

	// Resultados finales
	fmt.Printf("\nEl campeón del mundial es: %s\n", equipos[0])
	fmt.Printf("Subcampeón: %s\n", equipos[1])
	fmt.Printf("Tercer lugar: %s\n", tercerLugar)
}

func main() {
	equipos := []string{
		"Brasil", "Argentina", "Francia", "Alemania", "España", "Inglaterra", "Portugal", "Holanda",
		"Uruguay", "Bélgica", "Croacia", "México", "EEUU", "Senegal", "Japón", "Corea del Sur",
	}

	// Validar si hay un número par de equipos
	if len(equipos)%2 != 0 {
		fmt.Println("Error: La cantidad de equipos debe ser par.")
		return
	}

	jugarMundial(equipos)
}
