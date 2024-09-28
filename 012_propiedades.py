class Persona:
    def __init__(self, nombre, edad):
        self.__nombre =nombre
        self._edad = edad
    
    @property  
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
        
    @nombre.deleter 
    def nombre(self):
        del self.__nombre
    
dalto = Persona("Lucas", 21)

nombre = dalto.nombre
print(nombre)

dalto.nombre = "Pepe, despues se elimino con deleter"

nombre = dalto.nombre
print(nombre)

del dalto.nombre 
#se elimino por eso el error
#nombre = dalto.nombre
#print(nombre)