print(" ")
print("Gutierrez Torres Paola 3w")
print(" ")
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"edad: {self.edad}")
    def resultado(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad {self.edad}. :)")
        else:
            print(f"{self.nombre} es menor de edad {self.edad}. Crece chaneke.")
Persona1 = Persona("Payola", 16)
Persona1.imprimir_info()
Persona1.resultado()

Persona2 = Persona("Wicho", 17)
Persona2.imprimir_info()
Persona2.resultado()
