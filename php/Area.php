<?php
function calcularArea($figura, $var1, $var2) {
    $pi = 3.1416;
    $res = 0;

    switch ($figura) {
        case "1": 
            $res = ($var1 * $var2) / 2;
            echo "El área del Rombo es: " . $res . "\n";
            break;
        case "2":
            $res = $var1 * $var2;
            echo "El área del Rectángulo es: " . $res . "\n";
            break;
        case "3": 
            $res = $var1 * $var1; 
            echo "El área del Cuadrado es: " . $res . "\n";
            break;
        case "4": 
            $res = (($var1 + $var2) / 2) * $var2; 
            echo "El área del Trapecio es: " . $res . "\n";
            break;
        default: 
            $res = $var1 * $pi;
            echo "Resultado: " . $res . "\n";
    }
}

// Ejemplo de uso
calcularArea("1", 5, 10); 
calcularArea("2", 5, 10); 
calcularArea("3", 4, 0);   
calcularArea("4", 5, 10); 
calcularArea("5", 7, 0);
?>