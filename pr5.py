print(" ")
print("Gutierrez Torres Paola 3w")
print(" ")
class Contacto:
    def __init__(self, nombre, telefono, email):
    #Inicializa un contacto con su nombre, teléfono y correo electrónico
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
    #Devuelve una representación del contacto en formato legible
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"


class Agenda:
    def __init__(self):
    #Inicializa una agenda vacía
        self.contactos = []

    def añadir_contacto(self):
    #Añadir un nuevo contacto a la agenda
        nombre = input("Introduce el nombre del contacto: ")
        telefono = input("Introduce el teléfono del contacto: ")
        email = input("Introduce el email del contacto: ")
        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)
        print("Contacto añadido con éxito.")

    def listar_contactos(self):
    #Muestra todos los contactos en la agenda
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self):
    #Busca un contacto por nombre
        nombre = input("Introduce el nombre del contacto a buscar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(contacto)
                encontrado = True
                break
        if not encontrado:
            print("No se encontró ningún contacto con ese nombre.")

    def editar_contacto(self):
    #Edita la información de un contacto existente
        nombre = input("Introduce el nombre del contacto a editar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                nuevo_nombre = input(f"Nuevo nombre (deja vacío para no cambiarlo): ")
                if nuevo_nombre:
                    contacto.nombre = nuevo_nombre
                nuevo_telefono = input(f"Nuevo teléfono (deja vacío para no cambiarlo): ")
                if nuevo_telefono:
                    contacto.telefono = nuevo_telefono
                nuevo_email = input(f"Nuevo email (deja vacío para no cambiarlo): ")
                if nuevo_email:
                    contacto.email = nuevo_email
                print("Contacto actualizado.")
                return
        print("No se encontró un contacto con ese nombre.")

    def cerrar_agenda(self):
    #Cierra la agenda y termina el programa
        print("Cerrando agenda. ¡Hasta luego!")
        exit()

    def menu(self):
    #Muestra el menú principal y maneja la interacción con el usuario
        while True:
            print("\n--- Menú de la Agenda ---")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Selecciona una opción (1-5): ")

            if opcion == '1':
                self.añadir_contacto()
            elif opcion == '2':
                self.listar_contactos()
            elif opcion == '3':
                self.buscar_contacto()
            elif opcion == '4':
                self.editar_contacto()
            elif opcion == '5':
                self.cerrar_agenda()
            else:
                print("Opción no válida, por favor selecciona una opción entre 1 y 5.")


# Crear una instancia de la agenda y mostrar el menú
agenda = Agenda()
agenda.menu()
