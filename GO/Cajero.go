package main

import (
	"fmt"
)

// Definición de la estructura Usuario
type Usuario struct {
	Nombre string
	Pin    int
	Saldo  int
}

// Definición de la estructura Banco
type Banco struct {
	Usuarios []Usuario
}

// Método para autenticar un usuario
func (b *Banco) Autenticar(nombre string, pin int) bool {
	for _, usuario := range b.Usuarios {
		if usuario.Nombre == nombre {
			if usuario.Pin == pin {
				fmt.Println("Estás logeado")
				return true
			}
			fmt.Println("Pin o nombre incorrecto")
			return false
		}
	}
	fmt.Println("El usuario no existe")
	return false
}

// Método para retirar dinero
func (b *Banco) SacarDinero(nombre string, monto int) {
	for i := range b.Usuarios {
		if b.Usuarios[i].Nombre == nombre {
			if b.Usuarios[i].Saldo < monto {
				fmt.Println("Saldo insuficiente")
				return
			}
			b.Usuarios[i].Saldo -= monto
			fmt.Println("El saldo disponible es:", b.Usuarios[i].Saldo)
			return
		}
	}
}

func main() {
	// Crear usuarios
	ana := Usuario{"Ana", 9872, 450}
	pablo := Usuario{"Pablo", 5555, 200}
	rodrigo := Usuario{"Rodrigo", 2222, 900}

	// Crear instancia del banco con usuarios
	banco := Banco{Usuarios: []Usuario{ana, pablo, rodrigo}}

	for {
		fmt.Println("Bienvenido al Banco, por favor, identifíquese.")
		fmt.Print("Introduzca el nombre: ")
		var nombre string
		fmt.Scan(&nombre)

		fmt.Print("Introduzca el PIN: ")
		var pin int
		fmt.Scan(&pin)

		if banco.Autenticar(nombre, pin) {
			for {
				fmt.Println("Por favor, elija una opción:\n 1. Sacar dinero\n 2. Terminar sesión.")
				var opcion string
				fmt.Scan(&opcion)

				if opcion == "1" {
					fmt.Print("Introduce cantidad a sacar: ")
					var saldo int
					fmt.Scan(&saldo)
					banco.SacarDinero(nombre, saldo)
				} else if opcion == "2" {
					fmt.Println("Saliendo del sistema.")
					break
				} else {
					fmt.Println("Opción incorrecta. Por favor, introduzca otra opción.")
				}
			}
		} else {
			fmt.Println("Usuario no autenticado. Por favor, introduzca nombre y PIN correctos.")
		}
	}
}
