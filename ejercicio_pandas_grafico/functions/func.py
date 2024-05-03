import pandas as pd
import matplotlib.pyplot as plt

# Funcion para hallar el promedio de las calificaciones
def promedio_calificaciones_asignaturas(calificaciones):
    try:

        # Creo un diccionario donde almacenar los promedios
        promedios_asignaturas = {}

        # Creo listas para almacenar notas por asignatura
        notas_matematicas = []
        notas_ciencias = []
        notas_historia = []

        # Itero las calificaciones
        for values in calificaciones:

            # Añado cada nota en su respectiva asignatura
            valor_matematica = values["matematicas"]
            valor_ciencias = values["ciencias"]
            valor_historia = values["historia"]
            notas_matematicas.append(valor_matematica)
            notas_ciencias.append(valor_ciencias)
            notas_historia.append(valor_historia)

        # Realizo el promedio de cada asinatura
        promedio_matematicas = (sum(notas_matematicas)) / len(notas_matematicas)
        promedio_ciencias = (sum(notas_ciencias)) / len(notas_ciencias)
        promedio_historia = (sum(notas_historia)) / len(notas_historia)
        
        # Almaceno cada asignatura en el diccionarios
        promedios_asignaturas["matematicas"] = promedio_matematicas
        promedios_asignaturas["ciencias"] = promedio_ciencias
        promedios_asignaturas["historia"] = promedio_historia

        return promedios_asignaturas
    except Exception as e:
       print(f"Error: {e}")
    

# Funcion para sacar el promedio de calificaciones de los estudiantes
def promedio_calificaciones_estudiantes(calificaciones):

    try:
        promedio_calificaciones = []
        # Coloco las calid¿ficacion en un dataFrame
        df = pd.DataFrame(calificaciones)
    
        # Recorro el dataFrame
        for index, values in df.iterrows():

            # Hallo el promedio y la agrega a mi lista
            promedio = (values["matematicas"] + values["ciencias"] + values["historia"]) / 3
            promedio_calificaciones.append(promedio)

        # Creo un dataFrame con la columna de los nombres
        data_frame = pd.DataFrame(df["nombre"])
        # Creo un dataFrame con la columna de los promedios
        data_frame["promedio"] = promedio_calificaciones

        return data_frame
    
    except Exception as e:
        print(f"Error: ({e})")

# Función para crear el gráfico
def crear_grafico(alumnos_promedios):

    try:
        # Defino el eje x e i con grafico tipo barras
        plt.bar(alumnos_promedios["nombre"], alumnos_promedios["promedio"])

        # Asigno titulos y nombres de los ejes
        plt.xlabel('Nombre de estudiantes') # definir el nombre del eje X
        plt.ylabel('Promedio') # definir el nombre del eje Y
        plt.title('Promedio de alumnos'); # definir el titulo de la grafica

        # Muestro el grafico
        plt.show()
    except Exception as e:
        print(f"Error: ({e})")