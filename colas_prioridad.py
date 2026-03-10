# Nodo de la cola de prioridad
class Nodo:
    def __init__(self, dato, prioridad):
        self.dato = dato
        self.prioridad = prioridad
        self.siguiente = None


# Clase Cola de Prioridad
class ColaPrioridad:
    def __init__(self):
        self.inicio = None


    # 1️ Verificar si está vacía
    def esta_vacia(self):
        return self.inicio is None


    # 2️ Insertar ordenado por prioridad
    def insertar(self, dato, prioridad):
        nuevo = Nodo(dato, prioridad)

         # Caso 1: lista vacía o debe ir al inicio
        if self.inicio is None or prioridad < self.inicio.prioridad:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
            return

        # Caso 2: Buscar posición correcta
        actual = self.inicio
        while actual.siguiente and actual.siguiente.prioridad <= prioridad:
            actual = actual.siguiente

        # Insertar en medio o final
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo


    # 3️ Atender (eliminar el primero)
    def atender(self):
        if self.esta_vacia():
            print("Cola vacía")
            return None

        eliminado = self.inicio
        self.inicio = self.inicio.siguiente
        return eliminado.dato


    # 4️ Mostrar elementos
    def mostrar(self):
        if self.esta_vacia():
            print("Cola vacía")
            return

        actual = self.inicio
        while actual:
            print(f"Dato: {actual.dato} | Prioridad: {actual.prioridad}")
            actual = actual.siguiente


    # 5️ Ver primero sin eliminar
    def ver_primero(self):
        if self.esta_vacia():
            return None
        return self.inicio.dato


    # 6️ Tamaño de la cola
    def tamano(self):
        contador = 0
        actual = self.inicio
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador


# 🔹 Ejemplo de uso
cola = ColaPrioridad()

cola.insertar("Juan", 3)
cola.insertar("Ana", 1)
cola.insertar("Carlos", 2)

print("Elementos en la cola:")
cola.mostrar()

print("\nAtendiendo:", cola.atender())

print("\nDespués de atender:")
cola.mostrar()