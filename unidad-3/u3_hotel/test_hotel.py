import unittest
import pytest #Instalarlo desde el cmd -> pip install pytest
import hotel_manager as hm

from hotel import(
    Habitacion,
    Cliente,
    Reserva
)

class TestHotelManager(unittest.TestCase):
    def setUp(self):
        global clientes, habitaciones, reservas
        clientes = []
        habitaciones = []
        reservas = []
        
    def test_eliminar_cliente(self):
        hm.agregar_cliente("Juan", "juan@gmail.com")
        hm.eliminar_cliente("juan@gmail.com")
        self.assertEqual(hm.get_clientes_count(), 0)
        
    def test_modificar_cliente(self):
        hm.agregar_cliente("Juan", "juan@gmail.com")
        hm.modificar_cliente("juan@gmail.com", "juan perez")
        self.assertEqual(hm.get_cliente_by_index(0).nombre, "juan perez")
        
    def test_modificar_habitacion(self):
        hm.agregar_habitacion(101, "sencilla", 1000)
        hm.modificar_habitacion(101, tipo="doble")
        self.assertEqual(hm.get_habitaciones_count(), 1)
        
    def test_eliminar_habitacion(self):
        hm.agregar_habitacion(101, "sencilla", 1000)
        hm.eliminar_habitacion(101)
        self.assertEqual(hm.get_habitaciones_count(), 0)
        
    def test_realizar_reserva(self):
        hm.agregar_cliente("juan", "juan@gmail.com")
        hm.agregar_habitacion(101, "sencilla", 1000)
        hm.realizar_reserva("juan@gmail.com", 101, "2023-05-01", "2023-05-03")
        self.assertEqual(hm.get_reservas_count(), 1)
        
        print("Clientes", clientes)
        print("Habitaciones", habitaciones)
        print("Reservas", reservas)
            
    def test_cancelar_reserva(self):
        hm.agregar_cliente("juan", "juan@gmail.com")
        hm.agregar_habitacion(101, "sencilla", 1000)
        hm.realizar_reserva("juan@gmail.com", 101, "2023-05-01", "2023-05-03")
        hm.cancelar_reserva("juan@gmail.com", 101)
        self.assertEqual(hm.get_reservas_count(), 0)
        