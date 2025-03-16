# Función que valida si dos números son iguales
def validar_numeros(a, b)
  # Compara si a es igual a b y devuelve true o false
  a == b
end

# Declaramos variables para almacenar los números
print "Introduzca un número: "
a = gets.chomp.to_i

print "Introduzca otro número: "
b = gets.chomp.to_i

# Llamamos a la función validar_numeros y almacenamos el resultado
resultado = validar_numeros(a, b)

# Evaluamos el resultado y mostramos el mensaje correspondiente
if resultado
  puts "Son iguales"
else
  puts "Son distintos"
end