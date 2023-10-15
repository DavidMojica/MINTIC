import calculadora

numero_1 = 55
numero_2 = 20
numero_0 = 0

#Suma
print(f"La suma de los numeros es {calculadora.sumar(numero_1, numero_2)}")

#Resta
print(f"La resta de los numeros es: {calculadora.restar(numero_1, numero_2)}")

#Multiplicar
print(f"La multiplicacion de los numeros es: {calculadora.multiplicar(numero_1, numero_2)}")

#Dividir entre cero - Inválido
print(f"La división de los numeros es: {calculadora.dividir(numero_1, numero_0)}")

#Dividir
print(f"La division de los numeros es: {calculadora.dividir(numero_1, numero_2)}")

# Print Output:
# La suma de los numeros es 75
# La resta de los numeros es: 35
# La multiplicacion de los numeros es: 1100
# La división de los numeros es: No es posible dividir por 0
# La division de los numeros es: 2.75