# Métodos de listas
# index(n) (devuelve el orden dentro de la lista del elemento "n")
# count (cuenta la cantidad de elementos)
# sort(reverse=False)
# append (agrega un valor al final)
# extend (agrega una lista entera de valores)
# insert(x, "n") (inserta el elemento "n" en la posicion "x")
# pop ("n") "saca" el elemento "n" y me lo devuelve como return
# reverse (invierte el orden dado)
# clear() (borra los elementos de la lista)

lista = list(range(100))
print(lista[0:100])
print(lista[0:100:1])
print(lista[::1])

lista = list(range(200))
print(lista[9:22])

lista = list(range(10))
print(lista[::2])

lista = list(range(20))
print(lista[9:20:2])

print(lista.clear())

temperatures = [20, 30, 40, 50, 60, 10, 0]
temperatures1 = [20, 30, 40, 50, 4]
temperature = 50

print("El maximo de temperatures es ", max(temperatures))
print("El minimo de temperatures es ", min(temperatures))

print("Son iguales ?", temperatures == temperatures1)
print(f"temperatures tiene {len(temperatures)} valores")
print(f"temperature es tipo {type(temperature)} valores")
print(f"temperatures es tipo {type(temperatures)} valores")

if type(temperature) == int:
    print("temperature es int")

if type(temperatures) == list:
    print("temperatures es list")


for item in temperatures:
    print(item)

temperatures[3] = 60
print(temperatures)

techList = ["Apple", "Google", "Microsoft", "Dell"]
techList.append("Uala")
print(techList[1:3])
print(len(techList))

techList.remove("Dell")
print(techList)

techList.insert(2, "Tesla")
print(techList)
print("Apple" in techList)
techList.clear()
print(techList)