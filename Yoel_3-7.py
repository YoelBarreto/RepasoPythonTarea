# Define la clase Car en Python 3. La clase tendrá como atributos “matrícula” (numérica) y “color”. 
# Crea un método imprimir y, además, dos métodos adicionales que elijas.

import random

# El “color” será para cada instancia un color aleatorio obtenido de esta lista: ["red", "white", "black", "pink", "blue"].
colores = ["red", "white", "black", "pink", "blue"]

class Car:
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color

    def arrancar(self):
        print(f"El coche con matrícula {self.matricula} y color {self.color} ha arrancado.")

    def frenar(self):
        print(f"El coche con matrícula {self.matricula} y color {self.color} ha frenado.")

    def imprimir(self):
        print(f"Matrícula: {self.matricula}, Color: {self.color}")

n = int(input("Introduce el número de coches a crear: "))

# En segundo lugar, haz que el programa pida un número “n” por teclado y se creen “n” instancias de la clase, donde cada instancia:
# Cada “matrícula” tendrá un número consecutivo desde 1 hasta “n”.
coches = []
for i in range(1, n + 1):
    color_aleatorio = random.choice(colores)
    coche = Car(matricula=i, color=color_aleatorio)
    coches.append(coche)

# Finalmente, el programa deberá imprimir los valores de las 10 primeras instancias. En caso de que “n” sea menor que 10, solo se imprimirán “n” instancias.
cantidad_a_imprimir = min(n, 10)
for coche in coches[:cantidad_a_imprimir]:
    coche.imprimir()
