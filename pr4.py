print(" ")
print("Gutierrez Torres Paola 3w")
print(" ")
class Calculadora:
    def __init__(self, num1, num2):
    #Inicializa los números con los cuales se va a operar
        self.num1 = num1
        self.num2 = num2

    def suma(self):
    #Realiza la suma de los dos números
        return self.num1 + self.num2

    def resta(self):
    #Realiza la resta de los dos números
        return self.num1 - self.num2

    def multiplicacion(self):
    #Realiza la multiplicación de los dos números
        return self.num1 * self.num2

    def division(self):
    #Realiza la división de los dos números, manejando la división por cero
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: No se puede dividir entre cero."

# Solicitar al usuario que ingrese dos valores enteros
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Crear una instancia de la clase Calculadora
calculadora = Calculadora(num1, num2)

# Realizar las operaciones y mostrar los resultados
print(f"La suma de {num1} y {num2} es: {calculadora.suma()}")
print(f"La resta de {num1} y {num2} es: {calculadora.resta()}")
print(f"La multiplicación de {num1} y {num2} es: {calculadora.multiplicacion()}")
print(f"La división de {num1} y {num2} es: {calculadora.division()}")
