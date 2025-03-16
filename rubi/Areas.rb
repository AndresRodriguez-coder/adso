# Solicitar al usuario la figura a calcular
puts "Seleccione la figura a calcular, 1 para Rombo, 2 para Rectángulo, 3 para Cuadrado, 4 para Trapecio: "
figura = gets.chomp

# Solicitar valores al usuario
print "Ingrese el primer valor: "
var1 = gets.to_i
print "Ingrese el segundo valor: "
var2 = gets.to_i

res = 0.0 # Variable para almacenar el resultado
pi = 3.1416

# Estructura case en lugar de switch
case figura
when "1"
  res = (var1 * var2) / 2.0
  puts "El Área del Rombo es: #{res}"
when "2"
  res = var1 * var2
  puts "El Área del Rectángulo es: #{res}"
when "3"
  res = var1 * var2
  puts "El Área del Cuadrado es: #{res}"
when "4"
  res = (var1 + var2) / 2.0 * var2 # Ajustar la fórmula para el trapecio
  puts "El Área del Trapecio es: #{res}"
elseS
  res = var1 * pi
  puts "Resultado usando pi: #{res}"
end