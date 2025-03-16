# Declaración de una variable entera
a = 2

# Estructura condicional if-else
if a == 2
  puts "a vale 2"
else
  puts "a es distinto de 2"
end

# Declaración de variables de diferentes tipos
nombre = "Ana"
edad = 28
ciudad = "Colombia"

# Uso de operadores lógicos (and, or, not)
if nombre == "Ana" && edad == 28 && ciudad == "Colombia"
  puts "Su nombre es Ana, tiene 28 años y es de Colombia"
elsif nombre == "Ana" && edad != 28
  puts "Su nombre es Ana y no tiene 28 años"
elsif nombre != "Ana" && edad == 28
  puts "Su nombre no es Ana y tiene 28 años"
else
  puts "No se llama Ana ni tiene 28 años"
end