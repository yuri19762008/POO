class MiClase:
    def __init__(self):
        #1 guion bajo privado simple con acceso 
        self._atributo_privado ="Valor"
        
        # doble guion bajo muy privado sin acceso self.__atributo_privado ="Valor"
        
    #metodo muy privado __hablar dos guiones
    def __hablar(self):
        print("hola como estas")

objeto = MiClase()

#print(objeto._atributo_privado)

print(objeto.__hablar)