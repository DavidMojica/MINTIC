precio = 50
denominaciones = [25, 10, 5]
ingresado = 0
adeudado = precio

while adeudado > 0:
    moneda = int(input("Ingresa una moneda de 25, 10 o 5 centavos: "))
    if moneda in denominaciones:
        ingresado += moneda
        adeudado -= moneda
        print(f"Resta {adeudado}")
    else:
        print("Moneda no aceptada.")
        
if ingresado > precio:
    cambio = ingresado - precio
    print(f"Cambio : {cambio})")