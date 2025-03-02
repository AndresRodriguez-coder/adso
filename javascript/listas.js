// Crear un array
let a = [1, 2, 3, 4];
console.log(a);

// Operar como si fuese un string (en este caso, un array)
console.log(a[0]);
console.log(a.slice(0, 2)); // Slicing

// Concatenar array con otro array
let b = [5, 6];
console.log(a.concat(b)); // O a + b

// Sustituir el valor de una posición
a[3] = 'Hola';
console.log(a);

// Usar el método push() para añadir un elemento
a.push(3);
console.log(a);

// Obtener la longitud del array
console.log(a.length);

// Verificar si un elemento está en el array
console.log(a.includes(5));
console.log(a.includes(1));