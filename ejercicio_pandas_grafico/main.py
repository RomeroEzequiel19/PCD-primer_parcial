# Importo las funciones a utilizar
from functions.func import promedio_calificaciones_asignaturas as prom_cal_asig
from functions.func import promedio_calificaciones_estudiantes as prom_cal_est
from functions.func import crear_grafico as graficar

# Valores de calificaciones
calificaciones = [
    {"nombre": "Juan", "matematicas": 85, "ciencias": 90,
    "historia": 75},
    {"nombre": "María", "matematicas": 70, "ciencias": 80,
    "historia": 85},
    {"nombre": "Pedro", "matematicas": 95, "ciencias": 75,
    "historia": 90},
    {"nombre": "Ana", "matematicas": 80, "ciencias": 85, "historia":
    80},
    {"nombre": "Luis", "matematicas": 75, "ciencias": 70,
    "historia": 95},
    {"nombre": "Sofía", "matematicas": 90, "ciencias": 85,
    "historia": 75},
    {"nombre": "Carlos", "matematicas": 85, "ciencias": 90,
    "historia": 80},
    {"nombre": "Elena", "matematicas": 70, "ciencias": 75,
    "historia": 85},
    {"nombre": "Javier", "matematicas": 80, "ciencias": 85,
    "historia": 90},
    {"nombre": "Laura", "matematicas": 75, "ciencias": 70,
    "historia": 95},
    {"nombre": "Diego", "matematicas": 90, "ciencias": 85,
    "historia": 75},
    {"nombre": "Paula", "matematicas": 85, "ciencias": 90,
    "historia": 80},
    {"nombre": "Carmen", "matematicas": 70, "ciencias": 75,
    "historia": 85}
]  

# Imprime el promedio por calificaciones
print("Promedio de las asignaturas",prom_cal_asig(calificaciones))

# Obtener promedio de los estudiantes
alumnos_promedios = prom_cal_est(calificaciones)
print(alumnos_promedios)

# Graficar promedios estudiantes
graficar(alumnos_promedios)
