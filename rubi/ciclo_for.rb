loop do
  # Solicitar el primer valor
  print "Ingrese el primer valor: "
  a = gets.chomp.to_i

  # Solicitar el segundo valor
  print "Ingrese el segundo valor: "
  c = gets.chomp.to_i

  # Calcular la potencia
  valor = a ** c

  # Mostrar el resultado
  puts "La potencia de #{a} sobre #{c} es: #{valor}"

  # Preguntar si desea continuar
  print "¿Desea calcular otra potencia? (s/n): "
  opcion = gets.chomp
  break if opcion.downcase != "s"
end