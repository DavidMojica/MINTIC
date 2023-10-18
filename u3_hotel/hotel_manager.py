import csv
import os
from hotel import Habitacion, Cliente, Reserva

#Archivos planos
habitaciones_file = 'u3_hotel/habitaciones.csv'
clientes_file = 'u3_hotel/clientes.csv'
reservas_file = 'u3_hotel/reservas.csv'

#Vars
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
    with open(habitaciones_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for habitacion in habitaciones:
            writer.writerow(['habitacion', habitacion.numero, habitacion.tipo, habitacion.precio])

    with open(clientes_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for cliente in clientes:
            writer.writerow(['cliente', cliente.nombre, cliente.correo])

    with open(reservas_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for reserva in reservas:
            writer.writerow(['reserva', reserva.cliente.correo, reserva.habitacion.numero, reserva.fecha_inicio, reserva.fecha_fin])
            
def cargar_datos():
    global habitaciones, clientes, reservas

    # Load habitaciones data
    if os.path.exists(habitaciones_file):
        with open(habitaciones_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == 'habitacion':
                    numero, tipo, precio = map(int, row[1:])
                    habitacion = Habitacion(numero, tipo, precio)
                    habitaciones.append(habitacion)

    # Load clientes data
    if os.path.exists(clientes_file):
        with open(clientes_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == 'cliente':
                    nombre, correo = row[1:]
                    cliente = Cliente(nombre, correo)
                    clientes.append(cliente)

    # Load reservas data
    if os.path.exists(reservas_file):
        with open(reservas_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == 'reserva':
                    correo_cliente, numero_habitacion, fecha_inicio, fecha_fin = row[1:]
                    cliente = next(c for c in clientes if c.correo == correo_cliente)
                    habitacion = next(h for h in habitaciones if h.numero == int(numero_habitacion))
                    reserva = Reserva(cliente, habitacion, fecha_inicio, fecha_fin)
                    reservas.append(reserva)