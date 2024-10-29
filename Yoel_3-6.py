# Crea una lista en la cual cada elemento de esa lista sea una lista con dos valores: tamaño y peso.

lista = [
# tamaño | peso
    [1.50, 90],
    [1.85, 110],
    [2.10, 136],
    [1.30, 78],
]

# Utilizando Key functions, haz que esta lista se ordene por mayor altura y, en caso de igualdad, por menor peso.

sorted(lista, key=lambda altura_peso: (-altura_peso[0], altura_peso[1]))


# Explica en comentarios qué es realmente la “key function”. Pista: en la ayuda se menciona: 
# “El valor del parámetro key debe ser una función (u otro callable) que tome un solo argumento y devuelva una clave para usar con fines de ordenación. 
# Esta técnica es rápida porque la función key se llama exactamente una vez por cada registro de entrada.”

# Resumido: La key function es un parametro que te ayuda a ordenar, como .sort() en una lista, solo que a comparación de sort() puede
# comparar en más magnitud. Además de que no modifica el contenido de la lista al usarlo.




