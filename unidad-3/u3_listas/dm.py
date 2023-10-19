def main():
    shoping_listas = []
    
    while True:
        print("---Lista de compras---\n1. Agregar articulo\n2. Eliminar artículo\n3. Ver lista\n 4. Salir")
        
        opc = input("Introduzca una opción: ")
        
        if opc == "1":
            shoping_listas.append(input("Nombre del articulo a agregar: ").lower())
        elif opc == "2":
            item = input("Nombre del articulo que quieres eliminar: ").lower()
            if item in shoping_listas:
                shoping_listas.remove(item)
            else:
                print("El item no se encuentra en la lista")
        elif opc == "3":
            print(shoping_listas)
        elif opc == "4":
            break
        else:
            print("No ingresó una opción válida")   
            
if __name__ == "__main__":
    main()