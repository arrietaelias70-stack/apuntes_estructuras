class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class Pila:
    def __init__(self):
        self.tope = None  # Único puntero necesario

    def esta_vacia(self):
        return self.tope is None

    def insertar(self, valor):  # Push
        nuevo = Nodo(valor)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def eliminar(self):  # Pop
        if self.esta_vacia():
            return None

        eliminado = self.tope
        self.tope = self.tope.siguiente
        return eliminado.valor

    def consultar_tope(self):
        if self.esta_vacia():
            return None
        return self.tope.valor

    def contar_elementos(self):
        contador = 0
        actual = self.tope
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def mostrar(self):
        actual = self.tope
        while actual:
            print(actual.valor)
            actual = actual.siguiente