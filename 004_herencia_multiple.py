#clase
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar (self):
        print("Hola, Estoy hablando un poco")
#clase
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return(f"Mi habilidad es: {self.habilidad}")

#HERENCIA MULTIPLE
class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre, edad, nacionalidad,habilidad,empresa,salario):
        Persona.__init__(self, nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        print (f'Hola, soy: {self.nombre},  {super().mostrar_habilidad()} y trabajo en {self.empresa}')

#herencia
class Estudiante(Persona):
    def __init__(self,nombre, edad, nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notas =notas
        self.universidad= universidad






roberto = EmpleadoArtista("Roberto",43,"argentino","Cantar","Google", 100000)

roberto.presentarse()