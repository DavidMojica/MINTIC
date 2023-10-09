def main():
    MENU = {
        "Baja taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    order_total = 0

    while True:
        try:
            item = input("Ingrese un artículo de su pedido (o 'CONTROL-D' para terminar): ").capitalize()
        except EOFError:
            break

        if item == "Control-D":
            print(f"El total de su pedido es ${order_total:.2f}")
            break
        elif item in MENU:
            order_total += MENU[item]
            print(f"+${MENU[item]:.2f}")
        else:
            print("Artículo inválido")

if __name__ == "__main__":
    main()
