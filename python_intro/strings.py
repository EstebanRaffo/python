from idlelib.iomenu import encoding

print("Intro Python")

# Strings

# player = input("enter your player: ")
# print("favorite player: " + player)
#
# yourAge = input("Age: ")
# birthYaner = 2021 - int(yourAge)
# print(birthYaner)
#
#
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
print(word.find('y'))
# print(word.replace("sentence", "number"))
# print(word.find("sentence"))
# word1 = word.__add__(" and word added")
# print(word1)
# print(word1.__contains__("and"))
# print(word.split())
#
# word = 'hola,que,tal,mundo'
# print(word.split(','))
#
#
# nombre = 'Antonio'
# edad = 25
# print("Hola {} feliz cumpleaños {}".format(nombre, edad))
#
# resultado = 10/3
# print("El resultado es {r}".format(r=resultado))
# print("El resultado es {r:1.2f}".format(r=resultado))
#
# # f-strings
# nombre = 'Antonio'
# edad = 25
# print(f"Buenos dias {nombre}, feliz {edad} cumpleaños")


print("a".isalnum())
print("a".isalpha())
print("a".isascii())
print("a".encode('utf-8'))
print(type("Ã³".encode()))
print(type("á".encode()))


import re


txt = "Está Anulado"
txt1 = "EstÃ¡ Anulado"
txt2 = "Ãºmero"
txt3 = "DescriÃ³ciÃ³n"

arrayTxt = txt.split()
for caracter in arrayTxt:
    print(caracter)

x = re.findall("Ã", txt)
y = re.findall("Ã", txt1)
z = re.findall("Ã", txt2)
w = re.findall("Ã", txt3)

print(txt.find('Ã'))
print(txt1.find('Ã'))
print(txt2.find('Ã'))
print(txt3.find('Ã'))

print(f"Se encontró {len(x)} coincidencias")
print(f"Se encontró {len(y)} coincidencias")
print(f"Se encontró {len(z)} coincidencias")
print(f"Se encontró {len(w)} coincidencias")

contiene_caracter_invalido = txt.find('Ã') >= 0
if not contiene_caracter_invalido:
    print("txt no contiene caracter invalido")
else:
    print("txt contiene caracter invalido")

contiene_caracter_invalido = txt1.find('Ã') >= 0
if not contiene_caracter_invalido:
    print("txt1 no contiene caracter invalido")
else:
    print("txt1 contiene caracter invalido")
