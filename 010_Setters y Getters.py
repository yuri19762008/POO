class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
    
    def get_nombre(self):
        return self._nombre #getter accede a una clase que es privada 

    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

dalto = Persona("Lucas", 21)

nombre = dalto.get_nombre()
print(nombre)

dalto.set_nombre("pepito")

nombre = dalto.get_nombre()
print(nombre)
