def mostrar_opciones
  puts "Seleccione operación a realizar:"
  puts "1. Suma"
  puts "2. Resta"
  puts "3. Multiplicación"
  puts "4. División"
  puts "5. Potencia"
  puts "6. Raíz"
  puts "7. Suma de potencias"
  puts "8. Promedio"
  puts "9. Comparación"
  print "Opción: "
end

# Mostrar opciones al usuario
mostrar_opciones
operacion = gets.chomp.to_i

# Pedir valores al usuario
print "Ingrese el primer valor: "
A = gets.chomp.to_f
print "Ingrese el segundo valor: "
B = gets.chomp.to_f

# Estructura de control case para seleccionar la operación
case operacion
when 1
  res = A + B
  puts "La suma de los números es: #{res}"
when 2
  res = A - B
  puts "La resta de los números es: #{res}"
when 3
  res = A * B
  puts "La multiplicación de los números es: #{res}"
when 4
  if B != 0
    res = A / B
    puts "La división de los números es: #{res}"
  else
    puts "Error: División por cero no permitida."
  end
when 5
  res = A**B
  puts "La potencia es: #{res}"
when 6
  if B != 0
    res = A**(1.0 / B)
    puts "La raíz es: #{res}"
  else
    puts "Error: No se puede calcular la raíz con exponente 0."
  end
when 7
  res = A**B + A**B
  puts "La suma de potencias es: #{res}"
when 8
  res = (A + B) / 2
  puts "El promedio de los dos números es: #{res}"
when 9
  if A == B
    puts "Los números son iguales: #{A}"
  elsif A > B
    puts "El número mayor es: #{A}"
  else
    puts "El número mayor es: #{B}"
  end
else
  puts "Opción no válida. Intente de nuevo."
end