peso = float(input("Por favor introduzca su peso en kg"))
altura = float(input("Por favor ingrese su altura en mts"))

imc = peso / (altura ** 2)
if imc < 18.5:
    resultado = "Bajo peso"
elif imc < 25:
    resultado = "Peso normal"
else:
    resultado = "Sobrepeso"
    
print(f"Su IMC es {imc:.1f}. Usted está en {resultado}")