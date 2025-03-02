const diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
};

//Acceder a los valores
console.log(diccionario.nombre);
console.log(diccionario["edad"]);

// Agregar
diccionario.profession = "Ingeniero";

//Modificar valores
diccionario.edad = 31;
console.log(diccionario);

//Eliminar elementos
delete diccionario.ciudad;
console.log(diccionario);