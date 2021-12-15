# No es modificable como una lista

tupla_colores = ("celeste", "blanco", "negro")
tupla_A = ("Fondo10", "A")
tupla_B = ("Fondo10", "A")
# tupla_C = tupla_B + ("C")
# print("tupla_C = ", tupla_C)
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