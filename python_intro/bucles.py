# for
numeros = range(10, 20)
for num in numeros:
    print(num)


numbers = range(5, 20, 2)
for number in numbers:
    print(number)

# break
for num in range(10):
    if(num == 5):
        break
    print(num)

# continue
for num in range(10):
    if(num == 6):
        continue
    print(num)


for numero1 in range(4):
    for numero2 in range(3):
        print(numero1, numero2)



# while
i = 0
while i < 5:
    print(i)
    print(i*"i")
    i += 1


valor = 1
fin = 10
while(valor < fin):
    print(valor)
    valor += 1
    if(valor == 5):
        break

valor = 0
fin = 10
while(valor < fin):
    valor += 1
    if(valor == 5):
        continue
    print(valor)
