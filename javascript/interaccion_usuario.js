// Solicitar información al usuario
let a = prompt('Escriba sus nombres completos:');
let b = prompt('Escriba sus apellidos completos:');
let c = prompt('Escriba su profesión:');
let d = parseInt(prompt('Escriba su año de nacimiento:'));

// Calcular la edad
let e = 2025 - d;

// Imprimir el resultado en la consola
console.log('El (La)', c, a, b, 'tiene', e, 'años');