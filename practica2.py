

class Paciente:
    def __init__(self, nombre, edad, sintoma_principal, nivel_urgencia, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.sintoma_principal= sintoma_principal
        self.nivel_urgencia = nivel_urgencia
        self.prioridad = prioridad
        self.siguiente = None

class Lista_atencion:
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
        
    def insertar(self, nombre, edad, sintoma_principal, nivel_urgencia, prioridad):
        nuevo = Paciente(nombre, edad, sintoma_principal, nivel_urgencia, prioridad)
        pocision=1

         # Caso 1: lista vacía o debe ir al inicio
        if self.inicio is None or prioridad < self.inicio.prioridad:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
            print(f"El paciente {nuevo.nombre} será atendido de: ",pocision)
            return

        # Caso 2: Buscar posición correcta
        actual = self.inicio
        while actual.siguiente and ((actual.siguiente.nivel_urgencia < nuevo.nivel_urgencia) or ((nuevo.nivel_urgencia==actual.siguiente.nivel_urgencia) and (nuevo.prioridad>=actual.siguiente.prioridad))): 
            actual = actual.siguiente
            pocision=pocision+1

        # Insertar en medio o final
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo
        print(f"El paciente {nuevo.nombre} será atendido de: ",pocision+1)
    
    

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
            print("\nSintoma principal : ", actual.sintoma_principal)
            print("\nPrioridad: ", actual.prioridad)
            print("\nNivel de Urgencia: ", actual.nivel_urgencia)
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
        print("Sintoma principal :", eliminado.sintoma_principal)
        print("Nivel de urgencia :", eliminado.nivel_urgencia)
        print("Prioridad:", eliminado.prioridad)

L_atencion=Lista_atencion()
    
print("Gestion de la atención de los pacientes: ")
while True:
        print("1. Registrar paciente:")
        print("2. Atender siguiente solicitud: ")
        print("3. Mostrar cola de espera: ")
        print("4. Salir del programa:")

        opcion=int(input("Ingresa una opcion: "))

        match opcion:
            case 1:
                nombre=str(input("Ingresa el nombre del paciente: "))
                edad=int(input("Ingresa la edad del paciente: "))
                sintoma_principal=str(input("Ingresa el sistoma principal del paciente: " ))
                nivel_urgencia=int(input("Ingresa el nivel de urgencia del paciente: "))
                while nivel_urgencia<1 or nivel_urgencia>5:
                    nivel_urgencia=int(input("Ingresa el nivel de urgencia del paciente: "))
                
                prioridad=L_atencion.calcula_prioridad(edad)
                L_atencion.insertar(nombre, edad, sintoma_principal, nivel_urgencia, prioridad)

            case 2:
                print("Siguiente paciente para atender")
                L_atencion.siguiente_solicitud()

            case 3:
                print("Pacientes en espera")
                L_atencion.mostrar_cola()

            case 4:
                print("Finalizando")

