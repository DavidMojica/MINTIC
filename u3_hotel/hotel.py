import re
from datetime import datetime

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        
class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        if not re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", correo):
            raise ValueError("Correo inválido")
        self.correo = correo
        
        
class Reserva:
    def __init__(self, cliente, habitacion, fecha_inicio, fecha_fin):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
        self.fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d').date()
        if self.fecha_inicio > self.fecha_fin:
            raise ValueError("Las fechas no son válidas")