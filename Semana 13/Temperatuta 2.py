def calcular_promedio_ciudades(ciudades, temperaturas):
    promedios = {}
    for ciudad_idx, ciudad_data in enumerate(temperaturas):
        temperaturas_totales = []
        for semana_data in ciudad_data:
            for dia in semana_data:
                # Validar la clave 'temp' y agregar a la lista
                if 'temp' in dia:
                    temperaturas_totales.append(dia['temp'])

        # Calcular el promedio solo si hay datos disponibles
        if temperaturas_totales:
            promedio_ciudad = sum(temperaturas_totales) / len(temperaturas_totales)
            promedios[ciudades[ciudad_idx]] = promedio_ciudad
        else:
            promedios[ciudades[ciudad_idx]] = "No hay datos disponibles"

    return promedios


# Datos proporcionados en el prompt
temperaturas_data = [
    # Guayaquill
    [
        [{"day": "Lunes", "temp": 18}, {"day": "Martes", "temp": 11}, {"day": "Miércoles", "temp": 16},
         {"day": "Jueves", "temp": 13}, {"day": "Viernes", "temp": 15}, {"day": "Sábado", "temp": 17},
         {"day": "Domingo", "temp": 14}],
        [{"day": "Lunes", "temp": 13}, {"day": "Martes", "temp": 15}, {"day": "Miércoles", "temp": 14},
         {"day": "Jueves", "temp": 16}, {"day": "Viernes", "temp": 12}, {"day": "Sábado", "temp": 15},
         {"day": "Domingo", "temp": 13}],
        [{"day": "Lunes", "temp": 16}, {"day": "Martes", "temp": 14}, {"day": "Miércoles", "temp": 15},
         {"day": "Jueves", "temp": 13}, {"day": "Viernes", "temp": 14}, {"day": "Sábado", "temp": 16},
         {"day": "Domingo", "temp": 12}],
        [{"day": "Lunes", "temp": 14}, {"day": "Martes", "temp": 13}, {"day": "Miércoles", "temp": 15},
         {"day": "Jueves", "temp": 14}, {"day": "Viernes", "temp": 16}, {"day": "Sábado", "temp": 13},
         {"day": "Domingo", "temp": 15}],
        [{"day": "Lunes", "temp": 12}, {"day": "Martes", "temp": 14}, {"day": "Miércoles", "temp": 13},
         {"day": "Jueves", "temp": 15}, {"day": "Viernes", "temp": 14}, {"day": "Sábado", "temp": 16},
         {"day": "Domingo", "temp": 13}],
        [{"day": "Lunes", "temp": 15}, {"day": "Martes", "temp": 13}, {"day": "Miércoles", "temp": 14},
         {"day": "Jueves", "temp": 12}, {"day": "Viernes", "temp": 15}, {"day": "Sábado", "temp": 14},
         {"day": "Domingo", "temp": 16}]
    ],
    # Ventanas
    [
        [{"day": "Lunes", "temp": 17}, {"day": "Martes", "temp": 18}, {"day": "Miércoles", "temp": 16},
         {"day": "Jueves", "temp": 19}, {"day": "Viernes", "temp": 17}, {"day": "Sábado", "temp": 18},
         {"day": "Domingo", "temp": 16}],
        [{"day": "Lunes", "temp": 16}, {"day": "Martes", "temp": 17}, {"day": "Miércoles", "temp": 19},
         {"day": "Jueves", "temp": 18}, {"day": "Viernes", "temp": 16}, {"day": "Sábado", "temp": 17},
         {"day": "Domingo", "temp": 15}],
        [{"day": "Lunes", "temp": 18}, {"day": "Martes", "temp": 16}, {"day": "Miércoles", "temp": 17},
         {"day": "Jueves", "temp": 19}, {"day": "Viernes", "temp": 15}, {"day": "Sábado", "temp": 18},
         {"day": "Domingo", "temp": 17}],
        [{"day": "Lunes", "temp": 16}, {"day": "Martes", "temp": 18}, {"day": "Miércoles", "temp": 17},
         {"day": "Jueves", "temp": 16}, {"day": "Viernes", "temp": 19}, {"day": "Sábado", "temp": 15},
         {"day": "Domingo", "temp": 17}],
        [{"day": "Lunes", "temp": 15}, {"day": "Martes", "temp": 17}, {"day": "Miércoles", "temp": 18},
         {"day": "Jueves", "temp": 16}, {"day": "Viernes", "temp": 17}, {"day": "Sábado", "temp": 19},
         {"day": "Domingo", "temp": 16}],
        [{"day": "Lunes", "temp": 17}, {"day": "Martes", "temp": 16}, {"day": "Miércoles", "temp": 18},
         {"day": "Jueves", "temp": 15}, {"day": "Viernes", "temp": 17}, {"day": "Sábado", "temp": 16},
         {"day": "Domingo", "temp": 18}]
    ],
    # Babahoyo
    [
        [{"day": "Lunes", "temp": 26}, {"day": "Martes", "temp": 27}, {"day": "Miércoles", "temp": 28},
         {"day": "Jueves", "temp": 26}, {"day": "Viernes", "temp": 27}, {"day": "Sábado", "temp": 29},
         {"day": "Domingo", "temp": 28}],
        [{"day": "Lunes", "temp": 27}, {"day": "Martes", "temp": 28}, {"day": "Miércoles", "temp": 26},
         {"day": "Jueves", "temp": 29}, {"day": "Viernes", "temp": 27}, {"Sábado": "temp", "temp": 28},
         {"day": "Domingo", "temp": 26}],
        [{"day": "Lunes", "temp": 28}, {"day": "Martes", "temp": 26}, {"day": "Miércoles", "temp": 27},
         {"day": "Jueves", "temp": 28}, {"day": "Viernes", "temp": 29}, {"day": "Sábado", "temp": 27},
         {"day": "Domingo", "temp": 26}],
        [{"day": "Lunes", "temp": 27}, {"day": "Martes", "temp": 28}, {"day": "Miércoles", "temp": 26},
         {"day": "Jueves", "temp": 27}, {"day": "Viernes", "temp": 28}, {"day": "Sábado", "temp": 29},
         {"day": "Domingo", "temp": 27}],
        [{"day": "Lunes", "temp": 26}, {"day": "Martes", "temp": 27}, {"day": "Miércoles", "temp": 28},
         {"day": "Jueves", "temp": 26}, {"day": "Viernes", "temp": 29}, {"day": "Sábado", "temp": 27},
         {"day": "Domingo", "temp": 28}],
        [{"day": "Lunes", "temp": 27}, {"day": "Martes", "temp": 28}, {"day": "Miércoles", "temp": 26},
         {"day": "Jueves", "temp": 29}, {"day": "Viernes", "temp": 27}, {"day": "Sábado", "temp": 28},
         {"day": "Domingo", "temp": 26}]
    ]
]
nombres_ciudades = ["Guayaquill", "Ventanas", "Babahoyo"]

# Llamada a la función
promedios_por_ciudad = calcular_promedio_ciudades(nombres_ciudades, temperaturas_data)

# Imprimir los resultados
for ciudad, promedio in promedios_por_ciudad.items():
    if isinstance(promedio, float):
        print(f"Temperatura promedio en {ciudad}: {promedio:.2f} grados")
    else:
        print(f"Temperatura promedio en {ciudad}: {promedio}")