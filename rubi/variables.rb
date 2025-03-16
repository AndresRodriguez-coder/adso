# Declaración de variables
a = 10
b = 4

# Multiplicación
puts "La primera variable es: #{a}"
puts "El signo de la operación es: *"
puts "La segunda variable es: #{b}"
c = a * b
puts "El resultado es: #{c}"
puts "Tipo de dato: Integer"

# División
puts "\nLa primera variable es: #{a}"
puts "El signo de la operación es: /"
puts "La segunda variable es: #{b}"
d = a.to_f / b.to_f # Conversión a float para precisión
puts "El resultado es: #{d}"
puts "Tipo de dato: Float"

# Suma
puts "\nLa primera variable es: #{a}"
puts "El signo de la operación es: +"
puts "La segunda variable es: #{b}"
c = a + b
puts "El resultado es: #{c}"
puts "Tipo de dato: Integer"

# Resta
puts "\nLa primera variable es: #{a}"
puts "El signo de la operación es: -"
puts "La segunda variable es: #{b}"
c = a - b
puts "El resultado es: #{c}"
puts "Tipo de dato: Integer"

# Potencia
puts "\nLa primera variable es: #{a}"
puts "El signo de la operación es: **"
puts "La segunda variable es: #{b}"
e = a ** b # Potencia en Ruby
puts "El resultado es: #{e}"
puts "Tipo de dato: Float"

# Módulo
puts "\nLa primera variable es: #{a}"
puts "El signo de la operación es: %"
puts "La segunda variable es: #{b}"
c = a % b
puts "El resultado es: #{c}"
puts "Tipo de dato: Integer"