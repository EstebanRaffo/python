# No es modificable como una lista

tupla_colores = ("celeste", "blanco", "negro")
tupla_A = ("Fondo10", "A")
tupla_B = ("Fondo10", "A")
# tupla_C = tupla_B + ("C")
# print("tupla_C = ", tupla_C)
print("¿Son iguales las tuplas? ", tupla_A == tupla_B)

print(tupla_colores)
print(tupla_colores[1])
print(len(tupla_colores))

for color in tupla_colores:
    print(color)