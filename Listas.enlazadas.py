class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Verificar si está vacía
    def esta_vacia(self):
        return self.cabeza is None

    # Insertar al inicio
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # Insertar al final
    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    # Insertar en una posición específica
    def insertar_posicion(self, dato, posicion):
        if posicion == 0:
            self.insertar_inicio(dato)
            return

        nuevo = Nodo(dato)
        actual = self.cabeza
        contador = 0

        while actual and contador < posicion - 1:
            actual = actual.siguiente
            contador += 1

        if actual is None:
            print("Posición fuera de rango")
            return

        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

    # Eliminar por valor
    def eliminar(self, dato):
        actual = self.cabeza

        if actual and actual.dato == dato:
            self.cabeza = actual.siguiente
            return

        anterior = None
        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            print("Elemento no encontrado")
            return

        anterior.siguiente = actual.siguiente

    # Buscar un elemento
    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0

        while actual:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        print("no se encuentra en la lisa ")

        return 

    # Mostrar la lista
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    # Obtener tamaño
    def tamano(self):
        contador = 0
        actual = self.cabeza

        while actual:
            contador += 1
            actual = actual.siguiente

        return contador


# 🔹 Prueba del programa
lista = ListaEnlazada()

lista.insertar_inicio(10)
lista.insertar_inicio(5)
lista.insertar_final(20)
lista.insertar_posicion(15, 2)

print("Lista:")
lista.mostrar()

print("Tamaño:", lista.tamano())

print("Buscar 15:", lista.buscar(15))

lista.eliminar(10)
print("Después de eliminar 10:")
lista.mostrar()