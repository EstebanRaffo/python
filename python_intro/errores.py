try:
    num1 = 5
    num2 = 0
    div = num1 / num2
    print(div)
except ZeroDivisionError:
    print("Divisor no valido")
except:
    print("Hubo un error")
else:
    print("En else va lo que se ejecuta despues de try si no hubo error")
finally:
    print("En finally va lo que se ejecuta siempre despues de try con o sin error")