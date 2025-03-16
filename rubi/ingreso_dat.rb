# Declaramos variables para almacenar los datos ingresados por el usuario
a = ""
b = ""
c = ""
d = 0
e = 0

# Solicitamos los nombres completos
print "Escriba sus nombres completos: "
a = gets.chomp

# Solicitamos los apellidos completos
print "Escriba sus apellidos completos: "
b = gets.chomp

# Solicitamos la profesión
print "Escriba su profesión: "
c = gets.chomp

# Solicitamos el año de nacimiento
print "Escriba su año de nacimiento: "
d = gets.chomp.to_i

# Calculamos la edad restando el año de nacimiento al año actual (2025)
e = 2025 - d

# Mostramos el mensaje final con los datos ingresados
puts "El (La) #{c} #{a} #{b} tiene #{e} años"