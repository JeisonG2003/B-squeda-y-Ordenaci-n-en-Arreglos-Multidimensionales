# JEISON TEOBALDO GARCIA ARREAGA
# Crear una matriz bidimensional (3×3) para el ejemplo
matriz_2d = [
    [4, 7, 6],
    [3, 1, 2],
    [8, 9, 5]
]

# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz):
    n = len(matriz)
    for i in range(n - 1):  #fila
        for j in range(n - i - 1):
            if matriz[j] > matriz[j + 1]:
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]


def mostrar(matriz):
    for fila in matriz:
        print(fila)


# Mostrar la matriz con la fila ordenada
print("______________Matriz original______________")
mostrar(matriz_2d)

print("______________ordenar matriz______________")
fila_ordenar = int(input("ingrese en numero de fila"))

ordenar_fila(matriz_2d[fila_ordenar])
print("valores matriz----------")
mostrar(matriz_2d)
