# En Python 3 los tipos simples pasan por valor y los compuestos por referencia. Crea un ejemplo con 3 funciones que:

# 1 Reciban 2 números y devuelvan la suma.

num1 = int(input("Numero 1:"))
num2 = int(input("Numero 2:"))
print(f"Suma: {num1 + num2}")

# 2 Reciban una lista y modifiquen esa misma lista (referencia) duplicando los valores de todos los elementos. No debe devolver nada.

lista = [1, 2, 3, 4, 5]

def doublelist(numeros):
    for i in range(0, len(numeros)):
        numeros[i] *= 2

doublelist(lista)
print(lista)

# 3 Reciban una lista y devuelvan una copia de esa misma lista (referencia) duplicando los valores de todos los elementos. La lista original no debe modificarse.

lista2 = [1, 2, 3, 4, 5]
copia = []

def dupelist(dupe):
    for i in range(0, len(lista2)):
        dupe.append(lista2[i])
    for i in range(0, len(dupe)):
        dupe[i] *= 2

dupelist(copia)
print(lista2)
print(copia)
