conjunto_colores = {"rojo", "verde", "azul"}
print(conjunto_colores)

if "azul" in conjunto_colores:
    print("azul esta en conjunto_colores")

for color in conjunto_colores:
    print(color)

print(len(conjunto_colores))

conjunto_colores.add("negro")
print(conjunto_colores)

conjunto_colores.remove("verde")
print(conjunto_colores)

conjunto_colores.add("blanco")
print(conjunto_colores)

print(type(conjunto_colores))