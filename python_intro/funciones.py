# lambda
resultado = lambda numero : numero + 30
print(resultado(10))

resultado2 = lambda numero1, numero2 : numero1 + numero2
print(resultado2(5, 8))

promedio = lambda num1, num2, num3 : (num1 + num2 + num3) / 3
print(promedio(3, 4, 7))


# range
def pares(maximo):
    for numero in range(maximo):
        if numero % 2 == 0:
            yield numero

maximo = 11
for numero in pares(maximo):
    print(numero)


# Filter
def positivo(numero):
    return numero > 0

print(positivo(5))
print(positivo(-1))

numeros = [4, -2, 3, -5, 7, -6]
filtro = filter(positivo, numeros)
resultado = list(filtro)
print(resultado)


# Map
def multiplicar(numero):
    return numero * 2

print(multiplicar(2))

numeros = [2, 4, 6]
mapeo = map(multiplicar, numeros)
resultado = list(mapeo)
print(resultado)

lista_resultado = list(map(lambda numero : numero * 2, numeros))
print(lista_resultado)


# Pasar Funcion como parametro a otra
def cuadrado(x):
    return x ** 2

def raiz_cuadrada(x):
    return x ** 0.5

def operar(func, *args):
    for n in args:
        print(func(n))

operar(cuadrado, 2, 3, 5)
operar(raiz_cuadrada, 9, 25, 64, 49)