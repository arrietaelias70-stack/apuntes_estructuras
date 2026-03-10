class nodo:
    def __init__(self,valor):
        self.valor=valor
        self.siguiente=None

class cola:
    def __init__(self):
        self.inicio=None
        self.tope=None

    def insertar(self,valor):
        nuevo=nodo(valor)
        if self.inicio==None:
            self.inicio=nuevo
            self.tope=nuevo
        else:
            self.tope.siguiente=nuevo
            self.tope=nuevo

    def imprimir(self):
        if self.inicio==None:
            print("La cola se encuentra vacia")
        else:
            actual=self.inicio
            while actual!=None:
                print(actual.valor)
                actual=actual.siguiente

    def eliminar(self):
        if self.inicio==None:
            print("La cola se encuentra vacia")
        else:
            valor_eliminado=self.inicio.valor
            self.inicio=self.inicio.siguiente
            if self.inicio == None:
                self.tope = None
            return valor_eliminado

    def contar(self):
        contador_de_elementos=0

        if self.inicio==None:
            print("La cola esta vacia tiene cero elementos")
        else:
            actual=self.inicio
            while actual!=None:
                contador_de_elementos+=1
                actual=actual.siguiente
            print("La cola tiene",contador_de_elementos,"elementos")

    def siguiente_en_salir(self):
        if self.inicio==None:
            print("La cola se encuentra vacia")
        else:
            return self.inicio.valor 
        
    def valida_cola_vacia(self):
        if self.inicio==None:
            return True
        else:
            return False


Lista_de_colas=cola()
Lista_de_colas.insertar(1)
Lista_de_colas.insertar(2)
Lista_de_colas.insertar(3)
Lista_de_colas.insertar(4)

print(Lista_de_colas.siguiente_en_salir())
print(Lista_de_colas.eliminar())
print("¿La cola está vacía?", Lista_de_colas.valida_cola_vacia())

contar=Lista_de_colas.contar()
Lista_de_colas.imprimir()