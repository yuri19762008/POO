class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro =Perro()

#polimorfismo de funcion
hacer_sonido(perro)
hacer_sonido(gato)

#print(perro.sonido())
#print(gato.sonido())
