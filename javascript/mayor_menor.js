// Un programa que lee dos números, los compara y dice cuál es mayor.

let a = parseInt(prompt("Introduzca el primer número:"));
let b = parseInt(prompt("Introduzca el segundo número:"));

if (a > b) {
    console.log("A es mayor que B");
} else if (b > a) {
    console.log("B es mayor que A");
} else {
    console.log("Son iguales");
}

// Leer un número impar
a = parseInt(prompt("Introduzca un número:"));

while (a % 2 === 0) {
    console.log("El número", a, "es par, introduzca otro número");
    a = parseInt(prompt("Introduzca un número:"));
}

console.log("El número", a, "es impar. Programa terminado.");

// Menú para seleccionar opciones
console.log("Menú");
while (true) {
    console.log("Escribe una opción: \n 1. Comparar dos números.\n 2. Introducir un número impar\n 3. Terminar programa");
    let opcion = prompt();

    if (opcion === '1') {
        let a = parseInt(prompt("Introduzca el primer número:"));
        let b = parseInt(prompt("Introduzca el segundo número:"));
        if (a > b) {
            console.log("A es mayor que B");
        } else if (b > a) {
            console.log("B es mayor que A");
        } else {
            console.log("Son iguales");
        }
    } else if (opcion === '2') {
        let a = parseInt(prompt("Introduzca un número:"));
        while (a % 2 === 0) {
            console.log("El número", a, "es par, introduzca otro número");
            a = parseInt(prompt("Introduzca un número:"));
        }
        console.log("El número", a, "es impar");
    } else if (opcion === '3') {
        console.log("Terminando programa...");
        break;
    } else {
        console.log("Opción no disponible");
    }
}

// Crear un diccionario de libros
let libros = {
    'Los pilares de la Tierra': '1989',
    'El Código Da Vinci': '2003'
};

// Recorrer los títulos de los libros
for (let titulo in libros) {
    console.log(titulo);
}

// Recorrer los años
for (let key in libros) {
    console.log(libros[key]);
}

// Mostrar tanto la clave como el valor
for (let key in libros) {
    console.log(key, libros[key]);
}

// Crear una lista de películas y mostrar los datos de la 3ª posición
let peliculas = [];

let x = { titulo: 'Star Wars', año: '1977', director: 'George Lucas' };
let y = { titulo: 'El Señor de los Anillos', año: '2001', director: 'Peter Jackson' };
let c = { titulo: 'Psicosis', año: '1960', director: 'Alfred Hitchcock' };

peliculas.push(x);
peliculas.push(y);
peliculas.push(c);

// Mostrar los datos de la 3ª película
if (peliculas.length > 2) {
    let pelicula = peliculas[2];
    console.log(pelicula.titulo, pelicula.año, pelicula.director);
}