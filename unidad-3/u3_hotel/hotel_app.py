import os 
import sys
import hotel_manager as hm
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    opcion = -100
    while opcion != 0:
        try:
            opcion = int(input("""
                               Bienvenido al hotel
                               Menu
                               1. Agregar cliente
                               2. Eliminar cliente
                               3. Modificar cliente
                               4. Agregar habitacion
                               5. Eliminar habitacion
                               6. Modificar habitacion
                               7. Realizar reserva
                               8. Cancelar reserva
                               0. Salir
                               """))
            
            if opcion == 1:
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                hm.agregar_cliente(nombre, correo)
                print(f"Cliente {nombre} creado")
            elif opcion == 2:
                correo = input("Correo: ")
                hm.eliminar_cliente(correo)
                print("Cliente eliminado")
            elif opcion == 3:
                correo = input("Correo: ")   
                nombre = input("Nuevo nombre: ")
                hm.modificar_cliente(correo, nombre) 
                print("Cliente modificado")
            elif opcion == 4:
                numero = int(input("Introduzca el numero de la habitacion: "))
                tipo = input("Tipo de habitacion: ")
                precio = float(input("Precio: "))
                hm.agregar_habitacion(numero,tipo,precio)
                print(f"Habitacion {numero} creada")
            elif opcion == 5:
                numero = int(input("Numero de habitacion: "))
                hm.eliminar_habitacion(numero)
                print(f"Habitacon {numero} eliminada")
            elif opcion == 6:
                numero = int(input("Numero de habitacion: "))
                tipo = input("Tipo de habitacion: ")
                precio = float(input("Nuevo precio: "))
                hm.modificar_habitacion(numero, tipo, precio)
                print(f"Habitacion {numero} modificada")
            elif opcion == 7:
                cliente = input("Correo del cliente: ")
                habitacion = int(input("Numero de habitacion: "))
                fecha_inicio = input("Fecha de inicio (AAAA-MM-DD): ")          
                fecha_fin = input("Fecha de fin (AAAA-MM-DD): ")
                hm.realizar_reserva(cliente, habitacion, fecha_inicio, fecha_fin)
                print(f"Reserva realizada")
            elif opcion == 8:
                cliente = input("Correo del cliente: ")
                habitacion = int(input("Numero de la habitacion"))
                hm.cancelar_reserva(cliente, habitacion)
                print("Reserva cancelada") 
                
            hm.guardar_datos()         
        except ValueError:
            print("Opcion no valida")
            

if __name__ == "__main__":
    hm.cargar_datos()
    main()