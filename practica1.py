

print("Sistema de gestión de libros biblioteca: ")

class Libro:
    def __init__(self, codigo_libro, nombre_libro):
        self.codigo = codigo_libro
        self.nombre=nombre_libro
        self.disponible=True
        self.siguiente = None

class Persona:
    def __init__(self, nombre, cedula, codigo_libro, nombre_libro ):
        self.nombre = nombre
        self.cedula=cedula
        self.codigo=codigo_libro
        self.nombre_libro=nombre_libro
        self.siguiente = None



class Lista_personas:

    def __init__(self):
        self.cabeza = None

    # Verificar si está vacía
    def esta_vacia(self):
        return self.cabeza is None
    
     # Insertar al final
    def insertar_final(self, nombre, cedula, codigo_libro, nombre_libro ):
        nuevo =Persona(nombre, cedula, codigo_libro, nombre_libro )
        if self.esta_vacia():
            self.cabeza = nuevo
            return
        
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def buscar_persona(self,cedula):
         # Buscar un elemento
        actual = self.cabeza
        while actual:
            if actual.cedula == cedula:
               return actual
            actual= actual.siguiente
        print("no se encuentra en la lisa ")

    def consulta_individual(self,cedula):
     persona_consultar=self.buscar_persona(cedula)
     print(f"\nInformación de: {persona_consultar.nombre}")
     print(persona_consultar.nombre, persona_consultar.cedula, "la persona tiene el libro: ", persona_consultar.nombre_libro, "con codigo: ", persona_consultar.codigo)

    def consulta_general(self):
        # Mostrar la lista
        actual = self.cabeza
        if actual==None:
            print("Sistema de gestión de libros biblioteca: ")


class Lista_personas:

    def __init__(self):
        self.cabeza = None

    # Verificar si está vacía
    def esta_vacia(self):
        return self.cabeza is None
    
     # Insertar al final
    def insertar_final(self, nombre, cedula, codigo_libro, nombre_libro ):
        nuevo =Persona(nombre, cedula, codigo_libro, nombre_libro )
        if self.esta_vacia():
            self.cabeza = nuevo
            return
        
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def buscar_persona(self,cedula):
         # Buscar un elemento
        actual = self.cabeza
        while actual:
            if actual.cedula == cedula:
               return actual
            actual= actual.siguiente
        print("no se encuentra en la lista ")

    def consulta_individual(self,cedula):
     persona_consultar=self.buscar_persona(cedula)
     print(f"\nInformación de: {persona_consultar.nombre}")
     print(persona_consultar.nombre, persona_consultar.cedula, "la persona tiene el libro: ", persona_consultar.nombre_libro, "con codigo: ", persona_consultar.codigo)

    def consulta_general(self):
        # Mostrar la lista
        actual = self.cabeza
        if actual==None:
         print("No hay informacion")
        while actual:
            print(actual.nombre, actual.cedula, "la persona tiene el libro: ", actual.nombre_libro, "con codigo: ", actual.codigo, end=" -> ")
            actual = actual.siguiente
        

    def eliminar_persona(self, cedula):
        actual = self.cabeza

        if actual and actual.cedula == cedula:
            self.cabeza = actual.siguiente
            return actual

        anterior = None
        while actual and actual.cedula != cedula:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            print("Elemento no encontrado")
            return
        anterior.siguiente = actual.siguiente
        return actual
        

class Lista_Biblioteca:
    def __init__(self):
        self.cabeza = None

    def insertar_Libro(self, codigo_libro, nombre_libro):
        nuevo = Libro(codigo_libro, nombre_libro)
        if self.cabeza==None:
            self.cabeza = nuevo
            return
        
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def libros_disponibles(self):
        actual=self.cabeza
        while actual:
            if actual.disponible==True:
                print(actual.nombre, actual.codigo)
            actual=actual.siguiente

    def libros_prestados(self):
        actual = self.cabeza
        while actual:
            if not actual.disponible:
                print(actual.nombre, actual.codigo)
            actual = actual.siguiente

    def buscar_libro(self,codigo_libro):
         # Buscar un libro
        actual = self.cabeza
        while actual:
            if actual.codigo == codigo_libro:
               return actual
            actual= actual.siguiente
        print("El libro no se encuentra ")

Listaparalibros=Lista_Biblioteca()
listaparapersona=Lista_personas()
Listaparalibros.insertar_Libro(6, "El libro de papi elias")

print("Sistema de gestión de libros biblioteca: ")

while True:
        print("1. Registrar un prestamo ")
        print("2. Registrar una devolución ")
        print("3. Realizar consulta por personas (individual-general) ")
        print("4. Libros disponibles ")
        print("5. Libros ocupados ")

        opcion=int(input("Ingresa una opcion: "))

        match opcion:

            case 1: 
                print("\n Registrar un prestamo: ")
                nombre=str(input("Ingresa el nombre de la persona: "))
                cedula=int(input("Ingresa el numero de identificación de la persona: "))
                codigo=int(input("Ingresa el codigo del libro a prestar: "))
                nombrelibro=str(input("Ingresa el nombre del libro: "))
                buscarlibro=Listaparalibros.buscar_libro(codigo)
                if buscarlibro and buscarlibro.disponible:
                 buscarlibro.disponible=False
                 listaparapersona.insertar_final(nombre, cedula, codigo, nombrelibro)
                else:
                    print("No se encuentra disponible este libro")

            case 2:
                print("\n Registrar una devolución: ")
                cedula=int(input("Ingresa el numero de identificación de la persona: "))
                eliminado=listaparapersona.eliminar_persona(cedula)

                if eliminado:
                    devolver=Listaparalibros.buscar_libro(eliminado.codigo)
                    devolver.disponible=True
                    print("Se ha registrado correctamente la devolucion")
                else:
                    print("No se encuentra un prestamo registrado a esta persona")

            case 3:
                print("Consulta individual (1)--Consulta General (2)")
                op=int(input("Ingresa una opcion: "))
                if op==1:
                    cedula=int(input("Ingresa el numero de identificación de la persona: "))
                    individual=listaparapersona.buscar_persona(cedula)
                    if individual:
                        listaparapersona.consulta_individual(cedula)
                    else:
                        print("Persona no encontrada")
            
            case 4:
                print("Libros Disponibles: ")
                Listaparalibros.libros_disponibles()

            case 5:
                print("Libros Ocupados: ")
                Listaparalibros.libros_prestados()





            

        







