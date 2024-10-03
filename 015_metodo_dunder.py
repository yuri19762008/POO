class Persona:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
    #indica cono quiero que devuelva en modo de lista     
    def __str__(self):
        return f'Persona(Nombre: = {self.nombre}, Edad: = {self.edad})'
    #reconstruye el objeto a eleccion
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'
    
lucas = Persona("Lucas",21)

print(lucas)
# Persona(Nombre: = Lucas, Edad: = 21)

repre = repr(lucas)
resultado = eval(repre)

print(resultado)
# Persona(Nombre: = Lucas, Edad: = 21)
