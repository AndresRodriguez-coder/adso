def jugar_mundial(equipos)
  fases = ["Octavos de final", "Cuartos de final", "Semifinal", "Final"]
  tercer_lugar = ""

  while equipos.length > 1
    fase = fases.shift  # Eliminar la fase actual
    puts "\n#{fase}"

    ganadores = []
    equipos.each_slice(2) do |equipo1, equipo2|
      goles1 = 0
      goles2 = 0

      loop do
        print "Goles de #{equipo1}: "
        goles1 = gets.chomp.to_i
        print "Goles de #{equipo2}: "
        goles2 = gets.chomp.to_i

        # Validación de entrada
        if goles1 == goles2
          puts "No se permiten empates. Introduzca un nuevo marcador."
          next
        end
        break
      end

      # Determinar ganador
      ganadores << (goles1 > goles2 ? equipo1 : equipo2)

      # Guardar el equipo que perdió en la semifinal para el tercer lugar
      if equipos.length == 4
        tercer_lugar = equipo1 if goles1 < goles2
        tercer_lugar = equipo2 if goles1 > goles2
      end
    end

    equipos = ganadores
  end

  # Resultados finales
  puts "\nEl campeón del mundial es: #{equipos[0]}"
  puts "Subcampeón: #{equipos[1]}"
  puts "Tercer lugar: #{tercer_lugar}"
end

# Lista de equipos
equipos = [
  "Brasil", "Argentina", "Francia", "Alemania",
  "España", "Inglaterra", "Portugal", "Holanda",
  "Uruguay", "Bélgica", "Croacia", "México",
  "EEUU", "Senegal", "Japón", "Corea del Sur"
]

# Validar si hay un número par de equipos
if equipos.length.odd?
  puts "Error: La cantidad de equipos debe ser par."
else
  jugar_mundial(equipos)
end