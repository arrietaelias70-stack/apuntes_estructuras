
class Persona:
    def __init__(self, nombre, edad, direccion, motivo, gravedad, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.motivo = motivo
        self.gravedad = gravedad
        self.prioridad = prioridad
        self.siguiente = None


class Cola_llamada:
    def __init__(self):
        self.inicio = None

    def esta_vacia(self):
        return self.inicio is None
    
    def calcula_prioridad(self,edad):

        if edad<12:
            return 1
        if edad>65:
            return 2
        else:
            return 3
        
    def ingresar_llamada(self, nombre, edad, direccion, motivo, gravedad, prioridad):
        nuevo=Persona(nombre, edad, direccion, motivo , gravedad ,prioridad )
        #  Insertar ordenado por prioridad
        # Caso 1: lista vacía o debe ir al inicio de la cola la persona
        if self.inicio is None or (nuevo.gravedad < self.inicio.gravedad) or (nuevo.gravedad==self.inicio.gravedad and nuevo.prioridad<self.inicio.prioridad):
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
            return

        # Caso 2: Buscar posición correcta
        actual = self.inicio
        while actual.siguiente and ((actual.siguiente.gravedad < nuevo.gravedad) or (actual.siguiente.gravedad==nuevo.gravedad and actual.siguiente.prioridad<nuevo.prioridad)):
            actual = actual.siguiente

        # Insertar en medio o final
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo
    
    def mostrar_cola(self):
        if self.inicio is None:
            print("No hay llamadas en la cola")
            return

        actual = self.inicio
        posicion = 1

        while actual:
            print("\nAtención de la llamada")
            print("\nNombre: ", actual.nombre)
            print("\nEdad: ", actual.edad)
            print("\nGravedad: ", actual.gravedad)
            print("\nPrioridad: ", actual.prioridad)
            print("\nPocisión: ", posicion)
            print("\n-----------------------")
            
            actual = actual.siguiente
            posicion += 1

    def siguiente_solicitud(self):
        if self.esta_vacia():
            print("No hay llamadas")
            return None
        eliminado = self.inicio
        self.inicio = self.inicio.siguiente
        print("\nSiguiente solicitud atendida")
        print("Nombre:", eliminado.nombre)
        print("Edad:", eliminado.edad)
        print("Dirección:", eliminado.direccion)
        print("Motivo:", eliminado.motivo)
        print("Gravedad:", eliminado.gravedad)

    

cola = Cola_llamada()

while True:

    print("\nMENÚ")
    print("1. Ingresar llamada")
    print("2. Pasar siguiente solicitud")
    print("3. Mostrar cola")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))
    while opcion<1 or opcion>4:
        opcion = int(input("Seleccione una opción: "))


    if opcion == 1:

        nombre = input("Ingresa el nombre completo: ")
        edad = int(input("ingresa la edad: "))
        while edad<=0:
            edad = int(input("ingresa la edad: "))

        direccion = input("Dirección: ")
        motivo = input("Ingresa el motivo de la llamada: ")
        gravedad = int(input(" Ingresa la gravedad (1-5): "))
        while gravedad<1 or gravedad>5:
            gravedad = int(input(" Ingresa la gravedad (1-5): "))
        prioridad=cola.calcula_prioridad(edad)

        cola.ingresar_llamada(nombre, edad, direccion, motivo, gravedad, prioridad)

    elif opcion == 2:
        cola.siguiente_solicitud()

    elif opcion == 3:
        cola.mostrar_cola()

    elif opcion == 4:
        print("Programa finalizado")
        break
        
           

    
