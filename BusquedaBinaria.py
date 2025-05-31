# Función que implementa el algoritmo de búsqueda binaria de forma recursiva
def binary_search(lista, objetivo, inicio, fin):
    # Condición de corte: si el inicio supera al fin, el elemento no está en la lista
    if inicio > fin:
        return -1

    # Calculamos el índice del elemento central
    centro = (inicio + fin) // 2

    # Si el valor del centro es igual al objetivo, lo encontramos
    if lista[centro] == objetivo:
        return centro
    # Si el valor del centro es menor al objetivo, buscamos en la mitad derecha
    elif lista[centro] < objetivo:
        return binary_search(lista, objetivo, centro + 1, fin)
    # Si el valor del centro es mayor, buscamos en la mitad izquierda
    else:
        return binary_search(lista, objetivo, inicio, centro - 1)


# --- Ejemplo de uso del algoritmo ---

# Lista ordenada (requisito fundamental para aplicar búsqueda binaria)
lista = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 20, 27, 34, 39, 50]

# Número que queremos buscar
numero_objetivo = 27

# Definimos el rango de búsqueda inicial (toda la lista)
inicio_busqueda = 0
fin_busqueda = len(lista) - 1

# Llamamos a la función y guardamos el resultado
resultado = binary_search(lista, numero_objetivo, inicio_busqueda, fin_busqueda)

# Mostramos el resultado
if resultado != -1:
    print(f"El número {numero_objetivo} se encuentra en la posición {resultado}.")
else:
    print(f"El número {numero_objetivo} NO se encuentra en la lista.")
