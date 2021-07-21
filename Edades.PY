"""print("")

mayor_edad = 0
menor_edad = 0
tercera_edad = 0

cont = 0

n = int(input("Ingresa la cantidad de personas para revisar su edad:\n"))
while cont == n:
    edad = int(input("Ingresa edad para evaluar:\n ", cont))
    if edad < 18:
        print("es menor de edad ", menor_edad = menor_edad + 1)
    elif edad >= 18 and edad <= 60:
        print("Es mayor de edad ", mayor_edad = mayor_edad + 1)
    elif edad >= 60:
        print("Es Tercera edad ", tercera_edad = tercera_edad + 1)
    
    cont = cont + 1

print("")

print("Menor de edad: ", menor_edad * n / 100)
print("mayor de edad: ", mayor_edad)
print("Tercera edad: ", tercera_edad)

print("") """


menorEdad=0
mayoredad=0
terceraedad=0
cont = 1
cantidad=int(input("cantidad de personas (n): "))
while cont <= cantidad:
    print("Ingresa 1 = menor Edad, 2 = mayor edad, 3 = tercera edad")
    rangoedad=int(input("rango edad (1 = menor de 18) (2 = entre 18 y 60) (3 = mayor de 60): "))
    if rangoedad==1:
        menorEdad+=1
    elif rangoedad==2:
        mayoredad+=1
    elif rangoedad==3:
        terceraedad+=1
    
    cont = cont +1
        

print("\nReporte FINAL:")
total=menorEdad+mayoredad+terceraedad
print("menor de edad: ", str(menorEdad), ", porcentaje: ", str(round(menorEdad/total*100,)))
print("mayor de 18 y menor de 60: " , str(mayoredad), ", porcentaje: ", str(round(mayoredad/total*100,1)))
print("mas de 60: ", str(terceraedad), ", porcentaje: ", str(round(terceraedad/total*100,1)))
print("TOTAL edades:",total)
    


