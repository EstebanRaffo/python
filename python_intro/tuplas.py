# No es modificable como una lista

tupla_colores = ("celeste", "blanco", "negro")
tupla_A = ("Fondo10", "A")
tupla_B = ("Fondo10", "B")
tupla_C = ("Fondo10", "C")

print("¿Son iguales las tuplas? ", tupla_A == tupla_B)

lista_tuplas = [("Fondo10", "Z"), ("Fondo10", "B"), ("Fondo10", "P")]
if tupla_A in lista_tuplas:
    print("tupla_A está en lista_tuplas")
else:
    print("tupla_A NO está en lista_tuplas")

if tupla_A not in lista_tuplas:
    print("tupla_A NO está en lista_tuplas")
else:
    print("tupla_A está en lista_tuplas")

print(tupla_colores)
print(tupla_colores[1])
print(len(tupla_colores))

for color in tupla_colores:
    print(color)


lista_tuplas_A = [tupla_A, tupla_B, tupla_C]
lista_tuplas_B = [tupla_B, tupla_A, tupla_C]
lista_tuplas_C = [tupla_C, tupla_B, tupla_A]

print(f"lista_tuplas_A: {lista_tuplas_A}")
print(f"lista_tuplas_B: {lista_tuplas_B}")
print(f"lista_tuplas_C: {lista_tuplas_C}")

for tuplaA, tuplaB, tuplaC in zip(lista_tuplas_A, lista_tuplas_B, lista_tuplas_C):
    print(f"tuplaA: {tuplaA[0]} {tuplaA[1]}")
    print(f"tuplaB: {tuplaB[0]} {tuplaB[1]}")
    print(f"tuplaC: {tuplaC[0]} {tuplaC[1]}")

