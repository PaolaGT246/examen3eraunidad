print(" ")
print("Gutierez Torres Paola 3w")
print(" ")
class Alumno:
    def __init__(self, nombre, nota):
    #datos del alumno
        self.nombre = nombre
        self.nota = nota

    def imprimir_info(self):
    #imprimir informacion
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
    #mensaje si aprobo o reprobo
        if self.nota >= 5:
            print(f"{self.nombre} ha aprobado con una nota de {self.nota}. ¡Felicidades!")
        else:
            print(f"{self.nombre} no ha aprobado, con una nota de {self.nota}. Necesita mejorar.")

#imprime nota
alumno1 = Alumno("Payola", 7.5)
alumno1.imprimir_info()
alumno1.resultado()

alumno2 = Alumno("Wicho", 4.3)
alumno2.imprimir_info()
alumno2.resultado()
