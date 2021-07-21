""" Ejercicio 7. Crea un programa que pida al usuario 10 números enteros, los guarde en un array y luego le pregunte 
de forma repetitiva qué número quiere buscar. Le responderá si dicho número estaba o no entre los datos que se habían 
introducido inicialmente. Dejará de repetirse cuando se introduzca el número 0. """

print("")

def buscar_numero(elemento, list):
    for i in range(len(list)):
        if list[i] == elemento:
            return True
    return False


print("")

lista = []
enteros = 0
cont = 1
while cont <= 10:
    num1 = int(input("Ingresa un valor:\n"))
    print("En la posicion: ", cont)
    print("")
    enteros = enteros + 1
    cont = cont + 1
    lista.append(enteros)
print("")    
print("Numeros ingresados por el usuario:\n", lista)
print("")
num2 = int(input("¿Que numero quieres buscar?:\n"))
while num2 != 0:
    if buscar_numero(num2, lista):
        print(num2, "Encontrado en la lista :D, busca otro: ")
        num2 = int(input("Ingresa otro numero para buscar:\n"))
    else:
        print(num2, "* NO Encontrado en la lista :S, busca otro: * ")
        num2 = int(input("Ingresa otro numero para buscar:\n"))


print("")