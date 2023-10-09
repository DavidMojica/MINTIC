edad   = 20
result = None

#Expresión ternaria
result = "Es mayor de edad" if edad > 18 else "No es mayor de edad"
print(f"Ternaria: {result}")

#If else convencional
if edad > 18:
    result = "Es mayor de edad"
else:
    result = "No es mayor de edad"
    
print(f"If-Else: {result}")
