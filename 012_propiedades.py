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
    
yuri = Persona("Lucas", 21)

nombre = yuri.nombre
print(nombre)

yuri.nombre = "Pepe, despues se elimino con deleter"

nombre = yuri.nombre
print(nombre)

del yuri.nombre 
#se elimino por eso el error
#nombre = yuri.nombre
#print(nombre)