print("")
print("Bienvenido, por favor ingresa tu nombre ")
print("")
nom = input()
print("")
print("Hola", nom,"Presiona enter para ver la inicial de tu nombre ")
enter = input()
print("La inicial de tu nombre es:", nom[0], "\nPresiona enter para saber la cantidad de palabras que tiene tu nombre")
enter = input()
print("La cantidad de letras de tu nombre es: ",len(nom), "\nPresiona enter para saber la ultima letra de tu nombre")
enter = input()
print("La ultima letra es: ", nom[-1])
print("")
print("Presiona enter para convertir tu nombre a Mayuscula ")
enter = input()
print("Tu nombre en Mayuscula: ", nom.upper())
print("")
print("Presiona enter para invertir tu nombre ")
enter = input()
print("Tu nombre invertido es: ", (nom)[::-1])
print("")
print("Las vocales de tu nombre son las siguientes, presiona enter ")
enter = input()
def vocales1(nom):
    vocales2 = "aeiouAEIOU"

    return [x for x in nom if x in vocales2]

texto = nom
print(vocales1(nom), " Cantidad: ", len(vocales1(nom)), "Vocales.")
print("")
