# Lista de nombres
names = ["Ana", "Pablo", "Diego", "Carmen"]

# Lista de diccionarios (array de hashes)
people = [
  { "nombre" => "Ana", "edad" => 28 },
  { "nombre" => "Pablo", "edad" => 35 },
  { "nombre" => "Luis", "edad" => 38 }
]

# Imprimir nombre y edad de cada persona
people.each do |person|
  puts person["nombre"]
  puts person["edad"]
end
puts people.inspect # Mostrar toda la lista

# Crear una nueva lista con solo los nombres
lista_names = people.map { |person| person["nombre"] }
puts lista_names.inspect

# Lista de números
numbers = [1, 2, 3, 4, 5]
numbers.map!.with_index { |number, i| number + 3 }
puts numbers.inspect