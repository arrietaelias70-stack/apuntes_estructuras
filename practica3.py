

class Persona:
    def __init__(self, nombre, edad, direccion, tipo_de_emergencia, gravedad, prioridad):
        self.nombre=nombre
        self.edad=edad
        self.direccion=direccion
        self.tipo_de_emergencia=tipo_de_emergencia
        self.prioridad=prioridad
        self.gravedad=gravedad
        self.siguiente=None


class Lista_llamada:
    def __init__(self):
        self.inicio = None

    # 1️ Verificar si está vacía
    def esta_vacia(self):
        return self.inicio is None
    
    def calcula_prioridad(self,edad):

        if edad<12:
            return 1
        if edad>65:
            return 2
        else:
            return 3
        
    def insertar(self, nombre, edad, direccion, tipo_de_emergencia, gravedad, prioridad):

        nuevo = Persona(nombre, edad, direccion, tipo_de_emergencia, gravedad, prioridad)

        # CASO 1: insertar al inicio
        if self.inicio is None or gravedad < self.inicio.gravedad or (gravedad == self.inicio.gravedad and prioridad < self.inicio.prioridad):
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
            return

        # CASO 2: buscar posición
        actual = self.inicio

        while actual.siguiente and (
            actual.siguiente.gravedad < nuevo.gravedad or
            (actual.siguiente.gravedad == nuevo.gravedad and actual.siguiente.prioridad < nuevo.prioridad)):
             actual = actual.siguiente
             pocision += 1

        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo
        
        actual = self.inicio
        posicion = 1
        while actual:
         if actual == nuevo:  # encontramos al paciente recién insertado
            print(f"La persona {nuevo.nombre} fue registrada y será atendida en la posición: {posicion}")
            break
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
            print("Direccion :", eliminado.direccion)
            print("Tipo de emergencia :", eliminado.tipo_de_emergencia)
            print("Gravedad: ", eliminado.gravedad)
            print("Prioridad:", eliminado.prioridad)
            self.unidad_a_enviar(eliminado.gravedad)

    def mostrar_cola(self):
         if self.inicio is None:
            print("No hay llamadas en la cola")
            return

         actual = self.inicio
         posicion = 1
         print("\nAtención de los pacientes")

         while actual:
            print("Nombre:", actual.nombre)
            print("Edad:", actual.edad)
            print("Direccion :", actual.direccion)
            print("Tipo de emergencia :", actual.tipo_de_emergencia)
            print("Gravedad: ", actual.gravedad)
            print("Prioridad:", actual.prioridad)
            self.unidad_a_enviar(actual.gravedad)#para imprimir y usar un metodo dentro de otro metodo de la misma clase
            print("Posicion: ", posicion) 
                
            actual = actual.siguiente
            posicion += 1

    def unidad_a_enviar(self, gravedad):
        match gravedad:
            case 1:
                print("La unidad a enviar sera: Multiples camiones de bomberos y equipo completo")
                
            case 2:
                print("La unidad a enviar sera: Camión de bomberos principal")

            case 3:
                print("La unidad a enviar sera: Unidad de rescate")

            case 4:
                print("La unidad a enviar sera: Unidad de inspección")

            case 5:
                print("La unidad a enviar sera: Asesoria teleonica o revisión basica")


    
        

Lista_de_llamadas=Lista_llamada()


while True:
    print("MENÚ DE ATENCION DE LAS LLAMADAS")
    print("1. Registrar emergencia")
    print("2. Atender siguiente emergencia y mostrar sus datos ")
    print("3. Mostrar cola de emergencias")
    print("4. Finalizar programa")

    try:
     opcion=int(input("Ingresa una opcion: "))

    except ValueError:
     print("Ingrese un valor correcto: ")


    match opcion:
        case 1:
            print("\nRegistrar emergencia")
            nombre=str(input("Ingresa el nombre de la persona: "))
            edad=int(input("Ingresa la edad de la persona: "))
            direccion=str(input("Ingresa la direccion de la persona: : " ))
            tipo_de_emergencia=str(input("Ingresa el tipo de emergencia: incendio, rescate, fuga de gas, etc "))
            gravedad=int(input("Ingresa el nivel de gravedad (1-5)"))
            while gravedad<1 or gravedad>5:
                gravedad=int(input("Ingresa el nivel de gravedad (1-5)"))
                        
            prioridad=Lista_de_llamadas.calcula_prioridad(edad)
            Lista_de_llamadas.insertar( nombre, edad, direccion, tipo_de_emergencia, gravedad, prioridad)

        case 2:
            Lista_de_llamadas.siguiente_solicitud()
            

        case 3:
            Lista_de_llamadas.mostrar_cola()

        case 4:
            print("programa finalizado")
            break











