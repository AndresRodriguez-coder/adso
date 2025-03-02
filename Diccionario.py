barcos = [
    {
        'nombre': 'Poseidón',
        'tipo': 'yate',
        'color': 'blanco',
        'año': 2015,
        'matrícula': 'BRC1234'
    },
    {
        'nombre': 'Nautilus',
        'tipo': 'submarino',
        'color': 'gris',
        'año': 2008,
        'matrícula': 'SUB5678'
    },
    {
        'nombre': 'Mistral',
        'tipo': 'velero',
        'color': 'azul',
        'año': 2020,
        'matrícula': 'VEL9012'
    },
    {
        'nombre': 'Leviatán',
        'tipo': 'buque de carga',
        'color': 'rojo',
        'año': 2012,
        'matrícula': 'CARG3456'
    }
]

barcos[0]['color'] = 'azul'

print(barcos[0])

for barco in barcos:
    print(barco)