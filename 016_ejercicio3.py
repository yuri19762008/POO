class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre =self.nombre +"_" + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**2)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**2)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
Goku = Personaje("goku", 100, 100)
Vegeta = Personaje("vegeta", 99, 99)
jiren = Personaje("Jiren",130,140)

gogeta = Goku + Vegeta
jireta = gogeta + jiren
print(gogeta)
print(jireta)
print(Goku)
print(Vegeta)
print(jiren)
