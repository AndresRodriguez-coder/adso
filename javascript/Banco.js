class Usuario {
    constructor(nombre, pin, saldo) {
        this.nombre = nombre;
        this.pin = pin;
        this.saldo = saldo;
    }
}

class Banco {
    constructor(usuarios = []) {
        this.usuarios = usuarios;
    }

    autenticar(nombre, pin) {
        for (let usuario of this.usuarios) {
            if (usuario.nombre === nombre) {
                if (usuario.pin === pin) {
                    console.log("¡Estás logueado!");
                    return true;
                } else {
                    console.log("Pin o nombre incorrecto.");
                    return false;
                }
            }
        }
        console.log("El usuario no existe.");
        return false;
    }

    sacarDinero(nombre, cantidad) {
        for (let usuario of this.usuarios) {
            if (usuario.nombre === nombre) {
                if (usuario.saldo < cantidad) {
                    console.log("Saldo insuficiente.");
                } else {
                    usuario.saldo -= cantidad;
                    console.log("El saldo disponible es: " + usuario.saldo);
                }
                return;
            }
        }
    }
}

// Crear usuarios
const ana = new Usuario("Ana", 9872, 450);
const pablo = new Usuario("Pablo", 5555, 200);
const rodrigo = new Usuario("Rodrigo", 2222, 900);

// Crear el banco con los usuarios
const banco = new Banco([ana, pablo, rodrigo]);

// Bucle principal
while (true) {
    console.log("Bienvenido al Banco, por favor, identifíquese.");
    let nombre = prompt("Introduzca su nombre:");
    let pin = parseInt(prompt("Introduzca su pin:"));

    if (banco.autenticar(nombre, pin)) {
        while (true) {
            let opcion = prompt("Por favor, elija una opción:\n1. Sacar dinero\n2. Terminar sesión");

            if (opcion === "1") {
                let cantidad = parseInt(prompt("Introduce cantidad a sacar:"));
                banco.sacarDinero(nombre, cantidad);
            } else if (opcion === "2") {
                console.log("Saliendo del sistema.");
                break;
            } else {
                console.log("Opción incorrecta. Por favor, introduzca otra opción.");
            }
        }
    } else {
        console.log("Usuario no autenticado. Por favor, introduzca nombre y pin correctos.");
    }
}