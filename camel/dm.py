camel_case = input("Ingrese un nombre")
snake_case = ''.join(['_' + char.lower() if char.isupper() else char for char in camel_case])
print(f"Nombre en snake case: {snake_case}")