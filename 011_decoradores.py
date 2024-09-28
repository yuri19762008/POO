def decorador(funcion):
    def funcion_moddificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
        funcion()
    return funcion_moddificada

# def saludo():
#     print("Hola Dalto")
    
# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    print("Hola dalto como andas")
saludo()