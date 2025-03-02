// Lista de nombres
let name = ['Ana', 'Pablo', 'Diego', 'Carmen'];

// Lista de objetos (diccionarios en Python)
let person = [];
let a = { nombre: 'Ana', edad: 28 };
let b = { nombre: 'Pablo', edad: 35 };
let c = { nombre: 'Luis', edad: 38 };

person.push(a, b, c);

// Recorrer la lista de personas
person.forEach(person1 => {
    console.log(person1.nombre);
    console.log(person1.edad);
    console.log(person);
});

// Crear lista de nombres
let lista_name = person.map(person2 => person2.nombre);
console.log(lista_name);

// Lista de números
let numbers = [1, 2, 3, 4, 5];
numbers = numbers.map(number => number + 3);
console.log(numbers);
