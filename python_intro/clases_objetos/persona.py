
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Me llamo {} y tengo {} años".format(self.nombre, self.edad))