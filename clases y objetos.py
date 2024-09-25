class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    #metodos
    def llamar(self):
        print(f'Esta haciendo un llamado desde un: {self.modelo}')
    
    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')
    
    

celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Apple","Iphone 15 pro","96MP")


celular1.llamar()
celular2.cortar()