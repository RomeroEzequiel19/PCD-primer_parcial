# Se crea un función para eliminar los duplicados y se recibe como parámetro la lista
def eliminar_duplicados(lista):
    # Ocurre en caso de que no haya errores
    try:
        # Se crea una lista vacía para cargar los elementos sin duplicar
        lista_sin_duplicados = []

        # Se itera cada elemento de la lista 
        for value in lista:
            # Se vefica que el elemento no se encuentra en la lista sin duplicados
            if(value not in lista_sin_duplicados):
                # Se añade el elemento
                lista_sin_duplicados.append(value)

        return lista_sin_duplicados
    #Ocorre en caso de que haya errores
    except Exception as e:
        print(f"Error: ({e})")

# Se crea uns lista
lista = [1, 2, 3, 4, 4, 5, 6, 6, 7]

# Se envía como argumento la lista a la función eliminar duplicados
resultado = eliminar_duplicados(lista)
print(resultado)