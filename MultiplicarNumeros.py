#Codigo que solicita al usuario que ingrese 3 numeros a multiplicar, imprime por pantalla el resultado, luego divide el resultado en 2 y lo muestra por pantalla

def multiplicar_numeros():
    return a * b * c

def sacar_promedio():
    return resultado / 2

a = int(input("Ingresa el primer numero\n"))
b = int(input("Ingresa el segundo numero\n"))
c = int(input("Ingresa el tercer numero\n"))

resultado = multiplicar_numeros()

print(("El resultado de la multiplicacion entre ") + str(a) + (" * ") + str(b) + (" * ") + str(c) + (" = ") + str(resultado))

resultado2 = float(sacar_promedio())

print(("El promedio de ") + str(resultado) + (" = ") + str(resultado2))

