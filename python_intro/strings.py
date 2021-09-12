print("Intro Python")

# Strings

player = input("enter your player: ")
print("favorite player: " + player)

yourAge = input("Age: ")
birthYaner = 2021 - int(yourAge)
print(birthYaner)


numero = 5
# print("El numero es: " + numero)
print("El numero es: " + str(numero))

cadena = '5'
numero = int(cadena)
print(type(numero))

cadena = '2.5'
numero_decimal = float(cadena)
print(type(numero_decimal))

cadena = 'Hola mundo'
print(cadena[5])
print(cadena[2:7])
print(cadena[2:])
print(len(cadena))

word = "This is a sentence"
print(word.upper())
print(word.lower())
print(word.find('s'))
print(word.replace("sentence", "number"))
print(word.find("sentence"))
word1 = word.__add__(" and word added")
print(word1)
print(word1.__contains__("and"))
print(word.split())

word = 'hola,que,tal,mundo'
print(word.split(','))


nombre = 'Antonio'
edad = 25
print("Hola {} feliz cumpleaños {}".format(nombre, edad))

resultado = 10/3
print("El resultado es {r}".format(r=resultado))
print("El resultado es {r:1.2f}".format(r=resultado))

# f-strings
nombre = 'Antonio'
edad = 25
print(f"Buenos dias {nombre}, feliz {edad} cumpleaños")
