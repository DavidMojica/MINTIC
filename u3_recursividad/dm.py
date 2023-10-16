def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
    
num = 5
resultado = factorial(num)
print(f"El factorial de {num} es: {resultado}") 
# Print Output:
# El factorial de 5 es: 120