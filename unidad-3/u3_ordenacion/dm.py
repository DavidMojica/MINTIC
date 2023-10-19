def seleccion_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
        
#ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
seleccion_sort(numeros)
print(numeros)

# Print Output:
# [11, 12, 22, 25, 34, 64, 90]