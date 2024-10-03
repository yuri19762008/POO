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
    
    #comportamiento cuando sumas los objetos 
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre , nuevo_valor)
    
    
lucas = Persona("Lucas ",21)
pedro = Persona("Pedro ", 30)
maria = Persona("Maria ", 18)

nueva_persona = lucas + pedro + maria
print(nueva_persona)
print(nueva_persona.edad)
print(nueva_persona.nombre)





