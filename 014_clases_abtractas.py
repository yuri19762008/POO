from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self,nombre,edad,sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print (f"hola, me llamo: {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad} ")
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy Trabajando en el rubro de: {self.actividad} ")
        
        
pedro = Estudiante(" Pedro ", 25, "maculino", "Programacion")
lucas = Trabajador(" lucas ", 21, "maculino", "Programacion")

lucas.presentarse()
lucas.hacer_actividad()
pedro.presentarse()
pedro.hacer_actividad()