//crear un conjunto
let conjunto = new Set([1,2,3,4,5,6]);
// Mostrar el tamaño del conjunto 
console.log(conjunto.size);

//Comprobar si un elemento esta en el conjunto
console.log(conjunto.has(3));
console.log(conjunto.has(8));

//Agregar valores
console.log(conjunto.add(8));
console.log(conjunto.add(9));

//Elimnar
conjunto.delete(2);
console.log(conjunto);

// Mostrar todos los elementos del conjunto
conjunto.forEach(valor => {
    console.log(valor); // 1, 3, 4, 5
});