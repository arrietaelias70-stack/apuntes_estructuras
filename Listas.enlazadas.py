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




#Todos los metodos:
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:

    def __init__(self):
        self.cabeza = None


# -------------------------------------------------
# Insertar al inicio
# -------------------------------------------------
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo


# -------------------------------------------------
# Insertar al final
# -------------------------------------------------
    def insertar_final(self, dato):

        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza

        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo


# -------------------------------------------------
# Insertar en posición
# -------------------------------------------------
    def insertar_posicion(self, dato, posicion):

        nuevo = Nodo(dato)

        if posicion == 0:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return

        actual = self.cabeza
        contador = 0

        while actual and contador < posicion - 1:
            actual = actual.siguiente
            contador += 1

        if actual:
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo


# -------------------------------------------------
# Insertar después de un valor
# -------------------------------------------------
    def insertar_despues_de(self, valor_buscar, dato):

        actual = self.cabeza

        while actual:

            if actual.dato == valor_buscar:
                nuevo = Nodo(dato)

                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo
                return

            actual = actual.siguiente


# -------------------------------------------------
# Insertar antes de un valor
# -------------------------------------------------
    def insertar_antes_de(self, valor_buscar, dato):

        nuevo = Nodo(dato)

        if self.cabeza.dato == valor_buscar:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return

        actual = self.cabeza

        while actual.siguiente and actual.siguiente.dato != valor_buscar:
            actual = actual.siguiente

        if actual.siguiente:
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo


# -------------------------------------------------
# Eliminar al inicio
# -------------------------------------------------
    def eliminar_inicio(self):

        if self.cabeza:
            self.cabeza = self.cabeza.siguiente


# -------------------------------------------------
# Eliminar al final
# -------------------------------------------------
    def eliminar_final(self):

        if self.cabeza is None:
            return

        if self.cabeza.siguiente is None:
            self.cabeza = None
            return

        actual = self.cabeza

        while actual.siguiente.siguiente:
            actual = actual.siguiente

        actual.siguiente = None


# -------------------------------------------------
# Eliminar por valor
# -------------------------------------------------
    def eliminar(self, dato):

        if self.cabeza is None:
            return

        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return

        actual = self.cabeza

        while actual.siguiente and actual.siguiente.dato != dato:
            actual = actual.siguiente

        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente


# -------------------------------------------------
# Buscar elemento
# -------------------------------------------------
    def buscar(self, dato):

        actual = self.cabeza

        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente

        return False


# -------------------------------------------------
# Contar nodos
# -------------------------------------------------
    def contar(self):

        actual = self.cabeza
        contador = 0

        while actual:
            contador += 1
            actual = actual.siguiente

        return contador


# -------------------------------------------------
# Mostrar lista
# -------------------------------------------------
    def mostrar(self):

        actual = self.cabeza

        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente

        print("None")


# -------------------------------------------------
# Invertir lista
# -------------------------------------------------
    def invertir(self):

        anterior = None
        actual = self.cabeza

        while actual:

            siguiente = actual.siguiente
            actual.siguiente = anterior

            anterior = actual
            actual = siguiente

        self.cabeza = anterior


# -------------------------------------------------
# Verificar si está vacía
# -------------------------------------------------
    def esta_vacia(self):

        return self.cabeza is None


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
