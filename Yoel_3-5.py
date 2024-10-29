# Pon un ejemplo de cómo pasar varios parámetros desde la consola a un programa Python 3.
# Pon un ejemplo de cómo hacer “sobrecarga de funciones” (funciones que pueden recibir varios números de parámetros),
# incluyendo el caso en que el número de parámetros no esté definido.

def sumar_inf(*argumentos):
    suma = 0
    for numero in argumentos:
        suma += numero
    return suma

sumar_inf(5, 8, 10, 4, 9, 1)

