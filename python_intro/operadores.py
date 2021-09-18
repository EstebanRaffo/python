# Aritmeticos
# Division decimal
num1 = 10
num2 = 5
div = num1 / num2
print(div)

# Cociente: Division Entera
num1 = 5
num2 = 2
cociente = num1 // num2
print(cociente)

# Potencia
num = 2
exp = num ** 3
num **= 3

print("num = " + str(num))
print("exp = " + str(exp))

# Logicos
num1 = 5
num2 = 6
print(not(num1 > num2))

# Identidad
print("Identidad")
frutas1 = ["pera", "anana"]
frutas2 = ["pera", "anana"]
frutas3 = frutas1
print(frutas3)

print(frutas3 is frutas1)
print(frutas1 is frutas2)

frutas3.append("manzana")
print(frutas1)
print(frutas3)
print(frutas3 is frutas1)
print(frutas3 is not frutas1)

# Pertenencia
print("Pertenencia")
print(frutas2)
print(frutas3)
print("anana" in frutas3)
# print(frutas2 in frutas3)
frutas4 = "naranja"
print(frutas4 in frutas3)
print(frutas4 not in frutas3)
