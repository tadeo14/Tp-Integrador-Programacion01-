
# Función que implementa el algoritmo de búsqueda lineal
def linear_search(lista, objetivo):
    # Recorremos todos los elementos de la lista uno por uno
    for i in range(len(lista)):
        # Si el elemento actual coincide con el objetivo, devolvemos su índice
        if lista[i] == objetivo:
            return i
    # Si terminamos de recorrer la lista y no encontramos el objetivo, devolvemos -1
    return -1

# Lista de números ordenada (aunque la búsqueda lineal no necesita que lo esté)
lista = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 20, 27, 34, 39, 50]

# Número que queremos buscar
numero_objetivo = 39

# Llamamos a la función de búsqueda lineal y guardamos el resultado
resultado = linear_search(lista, numero_objetivo)

# Verificamos si el número fue encontrado y mostramos el resultado
if resultado != -1:
    print(f"El número {numero_objetivo} se encuentra en la posición: {resultado}")
else:
    print(f"El número {numero_objetivo} NO se encuentra en la lista.")
