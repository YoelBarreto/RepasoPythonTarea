"""
Explica y pon un ejemplo sencillo de una función lambda en Python 3.
Una función lambda es una función pequeña y anónima que se define en una sola línea. Se utiliza para operaciones simples que no necesitan un nombre explícito
"""

# Una funcion lambda es como una funcion pero muy corta, casi siempre se define en una sola linea y se utiliza para hacer operaciones simples

suma = lambda x, y: x + y
resultado = suma(3, 2)
print(resultado)

"""
Después, pon un ejemplo que utilice las funciones de Python:
Usando “map()” (y “list()” e “int()” como apoyo para convertir a lista y a números enteros), 
lee desde teclado una cadena de texto formada por números separados por espacios y transfórmala en una lista formada por números enteros.
"""

entrada = input("Ingresa números separados por espacios: ")

numeros = list(map(int, entrada.split()))
print("Lista original:", numeros)

"""
Usando “filter()”, elimina de la cadena anterior los números menores que 10.
"""

numeros_filtrados = list(filter(lambda x: x >= 10, numeros))
print("Números mayores o iguales a 10:", numeros_filtrados)

# Con la cadena resultante y usando “reduce()”, devuelve la multiplicación de los elementos de la lista.

resultado_multiplicacion = reduce(lambda x, y: x * y, numeros_filtrados)
print("Resultado de la multiplicación:", resultado_multiplicacion)
