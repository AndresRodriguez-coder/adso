# Definición de la clase Usuario
class Usuario
  attr_accessor :nombre, :pin, :saldo

  def initialize(nombre, pin, saldo)
    @nombre = nombre
    @pin = pin
    @saldo = saldo
  end
end

# Definición de la clase Banco
class Banco
  attr_accessor :usuarios

  def initialize
    @usuarios = []
  end

  # Método para autenticar un usuario
  def autenticar(nombre, pin)
    @usuarios.each do |usuario|
      if usuario.nombre == nombre
        if usuario.pin == pin
          puts "Estás logeado"
          return true
        end
        puts "Pin o nombre incorrecto"
        return false
      end
    end
    puts "El usuario no existe"
    false
  end

  # Método para retirar dinero
  def sacar_dinero(nombre, monto)
    @usuarios.each do |usuario|
      if usuario.nombre == nombre
        if usuario.saldo < monto
          puts "Saldo insuficiente"
          return
        end
        usuario.saldo -= monto
        puts "El saldo disponible es: #{usuario.saldo}"
        return
      end
    end
  end
end

# Crear usuarios
ana = Usuario.new("Ana", 9872, 450)
pablo = Usuario.new("Pablo", 5555, 200)
rodrigo = Usuario.new("Rodrigo", 2222, 900)

# Crear instancia del banco con usuarios
banco = Banco.new
banco.usuarios.push(ana, pablo, rodrigo)

loop do
  puts "Bienvenido al Banco, por favor, identifíquese."
  print "Introduzca el nombre: "
  nombre = gets.chomp

  print "Introduzca el PIN: "
  pin = gets.chomp.to_i

  if banco.autenticar(nombre, pin)
    loop do
      puts "Por favor, elija una opción:\n 1. Sacar dinero\n 2. Terminar sesión."
      opcion = gets.chomp

      if opcion == "1"
        print "Introduce cantidad a sacar: "
        saldo = gets.chomp.to_i
        banco.sacar_dinero(nombre, saldo)
      elsif opcion == "2"
        puts "Saliendo del sistema."
        break
      else
        puts "Opción incorrecta. Por favor, introduzca otra opción."
      end
    end
  else
    puts "Usuario no autenticado. Por favor, introduzca nombre y PIN correctos."
  end
end