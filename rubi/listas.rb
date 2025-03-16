# Declaramos una lista de enteros
numeros = [10, 20, 30, 40, 50]

# Agregar elementos al inicio y al final
numeros.unshift(5)  # Agregar al inicio
numeros.push(60)    # Agregar al final

# Imprimir la lista de números
puts "Lista de números:"
numeros.each do |num|
  print "#{num} "
end