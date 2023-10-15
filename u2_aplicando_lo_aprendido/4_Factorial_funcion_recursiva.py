def factorial(x):
    """Explicación: 
     En cada llamada recursiva, se multiplica el número actual
     por el factorial del número anterior (x - 1) hasta llegar a 1
    """
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

num = 8
print(f"El factorial de {num} es {factorial(num)}")

# Print Output:
# El factorial de 8 es 40320