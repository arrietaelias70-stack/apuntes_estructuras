
print("Sistema de gestión hotel")

class Habitacion:
    def __init__(self, numero):
        self.numero=numero
        self.disponible=True
        self.siguiente=None

class Huesped:
    def __init__(self,cedula, nombre, habitacion):
        self.cedula=cedula
        self.nombre=nombre
        self.habitacion=habitacion
        self.siguiente=None

#-----------------creación de listas---------------------------

class ListaHabitaciones:
    def __init__(self):
        self.cabeza= None
    
    def agregar_habitacion(self,numero):
        nueva=Habitacion(numero)

        if self.cabeza is None:
            self.cabeza=nueva
            return
        
        actual=self.cabeza
        while actual.siguiente:
            actual=actual.siguiente

        actual.siguiente=nueva

    def buscar_habitacion(self, numero):
        actual=self.cabeza

        while actual:
            if (actual.numero==numero):
                return actual
            actual=actual.siguiente
        return None
    
    def listar_disponibles(self):
        actual = self.cabeza
        print("\nHABITACIONES DISPONIBLES")
        while actual:
            if actual.disponible:
                print(actual.numero)
            actual = actual.siguiente

    def listar_ocupadas(self):
        actual = self.cabeza
        print("\nHABITACIONES OCUPADAS")
        while actual:
            if not actual.disponible:
                print(actual.numero)
            actual = actual.siguiente



class ListaHuespedes:
    def __init__(self):
        self.cabeza = None

    def registrar_entrada(self, cedula, nombre, habitacion):
        nuevo = Huesped(cedula, nombre, habitacion)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        print("El cliente ha sido registrado")

    def buscar_huesped(self, cedula):
        actual = self.cabeza
        while actual:
            if actual.cedula == cedula:
                return actual
            actual = actual.siguiente
        return None
    
    def registrar_salida(self, cedula):
        huesped = self.buscar_huesped(cedula)
        if huesped:
            print(f" Ha sido registrada la salida del huesped {huesped.nombre}")
            return huesped
        else:
            print(" Huésped no encontrado")
            return None
        
    def eliminar_huesped(self, cedula):
     if self.cabeza is None:
        return None

     if self.cabeza.cedula == cedula:
        eliminado = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return eliminado

     actual = self.cabeza
     while actual.siguiente:
        if actual.siguiente.cedula == cedula:
            eliminado = actual.siguiente
            actual.siguiente = actual.siguiente.siguiente
            return eliminado
        actual = actual.siguiente

     return None
    

    def consulta_individual(self, cedula):
        huesped = self.buscar_huesped(cedula)
        if huesped:
            print("\n Consulta individual")
            print(huesped.cedula, huesped.nombre, huesped.habitacion)
        else:
            print(" No se encontró ese huesped")
 
    def consulta_total(self):
        actual = self.cabeza
        print("\n Lista de huespedes por orden de llegada")
        while actual:
            print(actual.cedula, actual.nombre, actual.habitacion)
            actual = actual.siguiente

Listaparahabitaciones=ListaHabitaciones()
Listaparahuespedes=ListaHuespedes()
numero1=1
numero2=2
numero3=3
numero4=4
Listaparahabitaciones.agregar_habitacion(numero1)
Listaparahabitaciones.agregar_habitacion(numero2)
Listaparahabitaciones.agregar_habitacion(numero3)
Listaparahabitaciones.agregar_habitacion(numero4)


print("Menú ")

while True:
    print("1.Registrar entrada ")
    print("2.Registrar Salida ")
    print("3.Consulta de Habitaciones")
    print("4.Consulta de huepedes")
    print("5.Salir del programa")

    opcion=int(input("Ingresa una opcion: "))
    while opcion<1 or opcion>5:
        opcion=int(input(("Ingresa una opcion: ")))

    if opcion==1:
        print("Ingrese datos del cliente: ")
        cedula = input("Cédula: ")
        nombre = input("Nombre: ")
        numero = int(input("Habitación: "))

        habi = Listaparahabitaciones.buscar_habitacion(numero)

        if habi and habi.disponible:
         habi.disponible = False
         Listaparahuespedes.registrar_entrada(cedula, nombre, numero)
        else:
                print("La Habitación no esta disponible")

    if opcion == 2:
     print("Registrar salida")

     cedula = input("Cédula del huésped: ")

     huesped = Listaparahuespedes.eliminar_huesped(cedula)

     if huesped:
        habi = Listaparahabitaciones.buscar_habitacion(huesped.habitacion)
        habi.disponible = True
        print(f" Se registro la salida de {huesped.nombre}")
     else:
        print("El huesped no ha sido encontrado")

    
    if opcion==3:
        print("1. Consulta individual")
        print("2. Consulta total")
        sub = input("Seleccione una opcion: ")

        if sub == "1":
            cedula = input("Cédula: ")
            Listaparahuespedes.consulta_individual(cedula)
        else:
            Listaparahuespedes.consulta_total()

    if opcion == 4:
            print("1. Habitaciones disponibles")
            print("2. Habitaciones ocupadas")
            sub = input("Seleccione: ")
            if sub == "1":
                Listaparahabitaciones.listar_disponibles()
            else:
                Listaparahabitaciones.listar_ocupadas()

    if opcion == 5:
            print(" Terminado")
            
            break




    



