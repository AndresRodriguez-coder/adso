def jugar_mundial(equipos):
    fases = ["Octavos de final", "Cuartos de final", "Semifinal", "Final"]
    
    while len(equipos) > 1:
        fase = fases.pop(0)
        print(f"\n{fase}")
        
        ganadores = []
        for i in range(0, len(equipos), 2):
            equipo1, equipo2 = equipos[i], equipos[i+1]
            print(f"{equipo1} vs {equipo2}")
            goles1 = int(input(f"Goles de {equipo1}: "))
            goles2 = int(input(f"Goles de {equipo2}: "))
            
            if goles1 > goles2:
                ganadores.append(equipo1)
            else:
                ganadores.append(equipo2)
        
        equipos = ganadores
    
    print(f"\n¡{equipos[0]} es el campeón del mundial!")

# Equipos iniciales
equipos = ["Brasil", "Argentina", "Francia", "Alemania", "España", "Inglaterra", "Portugal", "Holanda", 
           "Uruguay", "Bélgica", "Croacia", "México", "EEUU", "Senegal", "Japón", "Corea del Sur"]

jugar_mundial(equipos)