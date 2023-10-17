import csv
from hotel import Habitacion, Cliente, Reserva

habitaciones = []
clientes = []
reservas = []

def get_cliente_by_index(index):
    return clientes[index]

def get_habitacion_by_index(index):
    return habitaciones[index]

def get_clientes_count():
    return len(clientes)

def get_habitaciones_count():
    return len(clientes)

def get_reservas_count():
    return len(reservas)

def agregar_habitacion(numero, tipo, precio):
    habitacion = Habitacion(numero, tipo, precio)
    habitaciones.append(habitacion)

def eliminar_habitacion(numero):
    global habitaciones
    habitaciones = [h for h in habitaciones if h.numero != numero]
    
def modificar_habitacion(numero, tipo=None, precio=None):
    for habitacion in habitaciones:
        if habitacion.numero == numero:
            if tipo:
                habitacion.tipo = tipo
            if precio:
                habitacion.precio = precio
            
def agregar_cliente(nombre, correo):
    cliente = Cliente(nombre, correo)
    clientes.append(cliente)
    
def eliminar_cliente(correo):
    global clientes 
    clientes = [c for c in clientes if c.correo != correo]
    
def modificar_cliente(correo, nombre=None):
    for cliente in clientes:
        if cliente.correo==correo:
            if nombre:
                cliente.nombre = nombre
                                
def realizar_reserva(cliente, habitacion, fecha_inicio, fecha_fin):
    reserva = Reserva(cliente, habitacion, fecha_inicio, fecha_fin)
    reservas.append(reserva)
    
def cancelar_reserva(cliente, habitacion):
    global reservas
    reservas = [r for r in reservas if r.cliente != cliente or r.habitacion != habitacion]
    
    
def guardar_datos():
    with open('hotel.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Guardar habitaciones
        for habitacion in habitaciones:
            writer.writerow(['habitacion', habitacion.numero, habitacion.tipo, habitacion.precio])

        # Guardar clientes
        for cliente in clientes:
            writer.writerow(['cliente', cliente.nombre, cliente.correo])

        # Guardar reservas
        for reserva in reservas:
            writer.writerow(['reserva', reserva.cliente.correo, reserva.habitacion.numero, reserva.fecha_inicio, reserva.fecha_fin])
            
def cargar_datos():
    global habitaciones, clientes, reservas

    with open('hotel.csv', mode='r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'habitacion':
                numero, tipo, precio = map(int, row[1:])
                habitacion = Habitacion(numero, tipo, precio)
                habitaciones.append(habitacion)
            elif row[0] == 'cliente':
                nombre, correo = row[1:]
                cliente = Cliente(nombre, correo)
                clientes.append(cliente)
            elif row[0] == 'reserva':
                correo_cliente, numero_habitacion, fecha_inicio, fecha_fin = row[1:]
                cliente = next(c for c in clientes if c.correo == correo_cliente)
                habitacion = next(h for h in habitaciones if h.numero == int(numero_habitacion))
                reserva = Reserva(cliente, habitacion, fecha_inicio, fecha_fin)
                reservas.append(reserva)