# Definimos una clase para los barcos
class Barco
  attr_accessor :nombre, :tipo, :color, :año, :matricula

  def initialize(nombre, tipo, color, año, matricula)
    @nombre = nombre
    @tipo = tipo
    @color = color
    @año = año
    @matricula = matricula
  end

  def to_s
    "#{@nombre}, Tipo: #{@tipo}, Color: #{@color}, Año: #{@año}, Matrícula: #{@matricula}"
  end
end

# Creamos un array de objetos Barco
barcos = [
  Barco.new("Poseidón", "yate", "blanco", 2015, "BRC1234"),
  Barco.new("Nautilus", "submarino", "gris", 2008, "SUB5678"),
  Barco.new("Mistral", "velero", "azul", 2020, "VEL9012"),
  Barco.new("Leviatán", "buque de carga", "rojo", 2012, "CARG3456")
]

# Modificamos el color del primer barco (Poseidón) a azul
barcos[0].color = "azul"

# Imprimimos el primer barco modificado
puts "Barco modificado: #{barcos[0]}"

# Iteramos sobre todos los barcos e imprimimos sus datos
puts "\nLista de barcos:"
barcos.each do |barco|
  puts barco
end