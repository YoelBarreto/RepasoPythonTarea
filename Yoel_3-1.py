# Prepara un ejemplo donde expliques cómo hacer en Python 3 lo siguiente: 

# 1 Clonar una lista.

lista = [1, 2, 3, 4, 5]
replica = []
for i in range(0, len(lista)):
    replica.append(lista[i])
print(replica)

# 2 ¿Cuál es la diferencia en Python entre “shallow copy” y “deep copy”?

# Shallow copy hace una copia superficial unicamente tomando referencias del original, además afectan al original
# Deep copy es una replica profunda copiada recursivamente y además no afecta a la original


# 3 Añadir un elemento a una lista.

replica.append(6)
print(replica)

# 4 Quitar un elemento de una lista.

replica.remove(replica[5])
print(replica)

# 5 Crear una nueva lista con los 4 últimos elementos de una lista.

replica4lastdigit = []
for i in range(1, len(lista)):
    replica4lastdigit.append(lista[i])
print(replica4lastdigit)

# 6 Convertir las palabras de una cadena (separadas por espacios) en una lista.

palabra = "palabra"
listapalabra = []

for j in list(palabra):
    listapalabra.append(j)
print(listapalabra)

# 7 Comentarios de una línea.

print("Si") # Haciendo el uso de la sintaxys que tiene python, para hacer un comentario es usando el "#" al inicio del comentario.

# 8 Comentarios multilínea.

print("No") # Dependiendo en el IDE que uno se encuentra usando atajos comentas varias lineas.
print("Tal vez") # Pero no existe otra manera mas que poner el "#" a la hora de comentar.
