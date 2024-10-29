# A partir de un contexto donde queremos almacenar un usuario y su contraseña, haz un ejemplo que explique cómo se haría:
import hashlib
# Usando una lista.

cuentalista = ["Yoel", "password"]

# Usando un diccionario.

cuentadicc = {
    "Yoel":"password"
}

# Al llenarse, las contraseñas deben pasarse a un formato Hash (por ejemplo, SHA-512).

def hash_password(password1):
    # return hashlib.sha512(password1).hexdigest()
    return hashlib.sha512(password1.encode()).hexdigest() # Es necesario usar encode() en la contraseña antes de usar el hexdigest()
codedpass = hash_password(cuentalista[1])
print(codedpass)

# El ejemplo debe llenar la lista con 5 usuarios/contraseña y hacer dos consultas.

listacuentas = [
    ["Alejandro", "1234yoel"],
    ["Francis", "50505010"],
    ["Yoel", "password"],
    ["Pepe", "almendra"],
    ["Antoñito", "peras901"]
]

print(f"{listacuentas[1][0]}: "+hash_password(listacuentas[1][1])) # Francis
print(f"{listacuentas[4][0]}: "+hash_password(listacuentas[4][1])) # Antoñito



