#1
class Animal(object):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def hacer_sonido(self):
        print(f"La clase animal hizo sonido.")
        
#2
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
        
    def hacer_sonido(self):
        print(f"Guau!")

#3      
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color
        
    def hacer_sonido(self):
        print(f"Miau!")
        
        
#4 
perro = Perro("Docker", 2, "Lobo Siberiano")
gato = Gato("Atenea", 4, "Gris")

perro.hacer_sonido()
gato.hacer_sonido()
# Print Output:
# Guau!
# Miau!

#5
def presentar_animal(Animal):
    print(f"-------------------------\nNombre del animal: {Animal.nombre} \nEdad del animal: {Animal.edad} años")
    Animal.hacer_sonido()
    
presentar_animal(perro)
presentar_animal(gato)
            
# Print Output:
# Guau!
# Miau!
# -------------------------
# Nombre del animal: Docker 
# Edad del animal: 2 años
# Guau!
# -------------------------
# Nombre del animal: Atenea 
# Edad del animal: 4 años
# Miau!