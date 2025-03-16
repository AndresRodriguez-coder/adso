# Función para calcular el voltaje (V = I * R)
def calcular_voltaje
  print "Ingrese la corriente (I) en amperios: "
  corriente = gets.chomp.to_f
  print "Ingrese la resistencia (R) en ohmios: "
  resistencia = gets.chomp.to_f
  puts "El voltaje V es: %.2f V" % (corriente * resistencia)
end

# Función para calcular la corriente (I = V / R)
def calcular_corriente
  print "Ingrese un voltaje en voltios: "
  voltaje = gets.chomp.to_f
  print "Ingrese la resistencia en ohmios: "
  resistencia = gets.chomp.to_f
  puts "La corriente I es: %.2f A" % (voltaje / resistencia)
end

# Función para calcular la resistencia (R = V / I)
def calcular_resistencia
  print "Ingrese el voltaje en voltios: "
  voltaje = gets.chomp.to_f
  print "Ingrese la corriente I en amperios: "
  corriente = gets.chomp.to_f
  puts "La resistencia R es: %.2f ohmios" % (voltaje / corriente)
end

# Menú de opciones
puts "=== Calculadora de la Ley de Ohm ==="
puts "1. Calcular Voltaje"
puts "2. Calcular Corriente"
puts "3. Calcular Resistencia"
print "Seleccione una opción (1-3): "
opcion = gets.chomp.to_i

# Estructura case para manejar la selección del usuario
case opcion
when 1
  calcular_voltaje
when 2
  calcular_corriente
when 3
  calcular_resistencia
else
  puts "Opción no válida."
end