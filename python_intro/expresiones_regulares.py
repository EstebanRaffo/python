# Expresiones regulares (search, findall, split, sub)

# search
texto = "Hola, mi nombre es Antonio"

import re

re.search("nombre", texto)
re.search("adios", texto)

resultado = re.search("nombre", texto)

if resultado:
    print("Cadena encontrada")
    inicio = resultado.start()
    fin = resultado.end()
    print("Desde posicion {} hasta {}".format(inicio, fin))
else:
    print("Cadena no encontrada")

# termina con
existe = re.search("Antonio$", texto)

if existe:
    print("Cadena encontrada: ", existe)
else:
    print("Cadena no encontrada")


# comienza con
existe = re.search("^Hola", texto)
print(existe)

# contiene
existe = re.search("mi.*es", texto)
print(existe)


# findall
texto = """
    El coche de Luis es rojo,
    el coche de Antonio es blanco,
    y el coche de Maria es rojo
    """

print(re.findall("coche.*rojo", texto))

# split
texto = "La silla es blanca y vale 80"
print(re.split("\s", texto))

# sub
print(re.sub("blanca", "roja", texto))