a = 2
if (a == 2){
    console.log("a vale 2")
}else{
    console.log("a es distinto de 2")
}
//Podemos concatenar condiciones con los operadores lógicos and, or y not


nombre = "Ana"
edad = 22
ciudad = "Colombia"

if (nombre == "Ana" && edad == 28 && ciudad == "Colombia"){
    console.log("La persona es Ana, tiene 28 años y vive en Colombia")
}else if(nombre == "Ana" && edad != 28){
    console.log("La persona es Ana pero no tiene 28 años")
}else if(nombre != "Ana" && edad == 28){
    console.log("La persona no es Ana pero tiene 28 años")
}else{
    console.log("La persona no es Ana y no tiene 28 años")
}
