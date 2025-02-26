#JEISON TEOBALDO GARCIA ARREAGA
# Matriz bidimensional de ejemplo
matriz_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return [i], [j]  # Retorna la posición (fila, columna)
    return None  # Si no se encuentra el valor

# Valor a buscar
valor_a_buscar = 8

# Llamar a la función y mostrar el resultado
resultado = buscar_valor(matriz_2d, valor_a_buscar)

if resultado:
    print(f"El valor {valor_a_buscar} se encuentra en la posición {resultado}.")
else:
    print(f"El valor {valor_a_buscar} no se encuentra en la matriz.")

