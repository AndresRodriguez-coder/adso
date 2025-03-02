// Crear un "array" que simula una tupla
let a = [1, 2, 3, 4];
console.log(a);

// Acceder al primer elemento
console.log(a[0]);

// Obtener una subarray (similar al slicing)
console.log(a.slice(0, 2));

// No podemos modificar el "array" como una tupla, pero podemos ver su tamaño
console.log(a.length);

// Verificar si un elemento está en el "array"
console.log(a.includes(5));
console.log(a.includes(1));

// Resumen: funciones y sintaxis similares a las listas, pero sin poder alterar valores o tamaño

// Convertir a un array (en este caso, ya es un array)
let b = Array.from(a);
console.log(b);

// Añadir un elemento al "array"
b.push(5);
console.log(b);