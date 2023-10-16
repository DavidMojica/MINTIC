import random
numeros = [random.randint(1,100) for _ in range(20)]
print(numeros)

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista)//2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    
    return quick_sort(izquierda) + medio + quick_sort(derecha)

numeros_ordenados = quick_sort(numeros)
print(numeros_ordenados) 

# Print Output:
# [53, 15, 80, 29, 68, 82, 75, 34, 81, 2, 25, 27, 58, 55, 63, 88, 28, 73, 53, 8]
# [2, 8, 15, 25, 27, 28, 29, 34, 53, 53, 55, 58, 63, 68, 73, 75, 80, 81, 82, 88]