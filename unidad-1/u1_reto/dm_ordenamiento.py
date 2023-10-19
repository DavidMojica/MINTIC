lista_desordenada = [5, 6, 1, 11, 4, 2, 1, 7, 2, 5, 75, 2]
lista_desordenada.sort()
print(lista_desordenada) #metodo sort

lista_desordenada = [5, 6, 1, 11, 4, 2, 1, 7, 2, 5, 75, 2]

for i in range(len(lista_desordenada)): #burbuja
    for j in range(i + 1, len(lista_desordenada)):
        if lista_desordenada[j] < lista_desordenada[i]:
            lista_desordenada[i], lista_desordenada[j] = lista_desordenada[j], lista_desordenada[i]

print(lista_desordenada)
      