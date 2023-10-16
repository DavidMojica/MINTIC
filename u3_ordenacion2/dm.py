import random

numeros = [random.randint(1,100) for _ in range(20)] #añadir 20 numeros aleatorios entreo 1 y 100
print(f"lista desordenada: {numeros}")

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                
                
bubble_sort(numeros)
print(f"Lista ordenada: {numeros}")

# Print Output: (es random)
# lista desordenada: [42, 75, 13, 65, 24, 11, 65, 65, 26, 97, 10, 73, 51, 35, 84, 56, 72, 93, 27, 70]
# Lista ordenada: [10, 11, 13, 24, 26, 27, 35, 42, 51, 56, 65, 65, 65, 70, 72, 73, 75, 84, 93, 97]