# numero par o impar recorriendo la regla

numero = int(input("ingrese un numero:\n"))
while numero > 0:
    if numero % 2 == 0:
        print("es par")
    else:
        print("Es impar")
numero = numero + 1

print(numero)