print(" ")
print("Gutierrez Torres Paola 3w")
print(" ")
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
    #Inicializa los lados del triángulo
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir_lado_mayor(self):
    #Imprime el lado con el tamaño mayor
        mayor_lado = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mayor del triángulo es: {mayor_lado}")

    def tipo_triangulo(self):
    #Determina el tipo de triángulo basado en la longitud de sus lados
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es Equilátero.")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El triángulo es Isósceles.")
        else:
            print("El triángulo es Escaleno.")

triangulo1 = Triangulo(5, 5, 5)
triangulo1.imprimir_lado_mayor()
triangulo1.tipo_triangulo()

triangulo2 = Triangulo(3, 4, 5)
triangulo2.imprimir_lado_mayor()
triangulo2.tipo_triangulo()

triangulo3 = Triangulo(6, 7, 6)
triangulo3.imprimir_lado_mayor()
triangulo3.tipo_triangulo()
