<?php
class Usuario {
    public $nombre;
    public $pin;
    public $saldo;

    public function __construct($nombre, $pin, $saldo) {
        $this->nombre = $nombre;
        $this->pin = $pin;
        $this->saldo = $saldo;
    }
}

class Banco {
    public $usuarios;

    public function __construct($usuarios = []) {
        $this->usuarios = $usuarios;
    }

    public function autenticar($nombre, $pin) {
        foreach ($this->usuarios as $usuario) {
            if ($usuario->nombre === $nombre) {
                if ($usuario->pin === $pin) {
                    echo "¡Estás logueado!\n";
                    return true;
                } else {
                    echo "Pin o nombre incorrecto.\n";
                    return false;
                }
            }
        }
        echo "El usuario no existe.\n";
        return false;
    }

    public function sacarDinero($nombre, $cantidad) {
        foreach ($this->usuarios as $usuario) {
            if ($usuario->nombre === $nombre) {
                if ($usuario->saldo < $cantidad) {
                    echo "Saldo insuficiente.\n";
                } else {
                    $usuario->saldo -= $cantidad;
                    echo "El saldo disponible es: " . $usuario->saldo . "\n";
                }
                return;
            }
        }
    }
}

// Crear usuarios
$ana = new Usuario("Ana", 9872, 450);
$pablo = new Usuario("Pablo", 5555, 200);
$rodrigo = new Usuario("Rodrigo", 2222, 900);

// Crear el banco con los usuarios
$banco = new Banco([$ana, $pablo, $rodrigo]);

// Bucle principal
while (true) {
    echo "Bienvenido al Banco, por favor, identifíquese.\n";
    $nombre = readline("Introduzca su nombre: ");
    $pin = (int)readline("Introduzca su pin: ");

    if ($banco->autenticar($nombre, $pin)) {
        while (true) {
            $opcion = readline("Por favor, elija una opción:\n1. Sacar dinero\n2. Terminar sesión\n");

            if ($opcion === "1") {
                $cantidad = (int)readline("Introduce cantidad a sacar: ");
                $banco->sacarDinero($nombre, $cantidad);
            } else if ($opcion === "2") {
                echo "Saliendo del sistema.\n";
                break;
            } else {
                echo "Opción incorrecta. Por favor, introduzca otra opción.\n";
            }
        }
    } else {
        echo "Usuario no autenticado. Por favor, introduzca nombre y pin correctos.\n";
    }
}
?>