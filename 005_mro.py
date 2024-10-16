class A:
    def hablar (self):
        print("hola desde A")
        
class F(A):
    def hablar (self):
        print("hola desde F")
        
class B(A):
    def hablar (self):
        print("hola desde B")
        
class C(F):
    def hablar (self):
        print("hola desde C")
        
class D(B,C):
    def hablar (self):
        print("hola desde D")
    
d = D()

print(D.mro())

d.hablar()

#especificar desde donde llamara la clase
A.hablar(d)
B.hablar(d)
C.hablar(d)
D.hablar(d)
F.hablar(d)