print(" ")
n = input("Ingresa un texto para saber cuantos cartacteres tiene\n")
cantidad_letras = len(n)
print("El texto ingresado contiene " + str(cantidad_letras) + " Caracteres ")
print(" ")
input("Presiona enter para saber la ultima letra del texto")
print(" ")
ultimo = n[cantidad_letras - 1]
print("El ultimo caracter del texto " + str(n) + " es " + ultimo + ", " + ultimo + " Se encuentra en la posicion " + str(cantidad_letras))
print(" ")
input("Presiona Enter para la siguiente actividad")
print(" ")
nombre1 = input("Ingresa tu primer nombre\n")
nombre2 = input("Ingresa tu segundo nombre\n")
apellido1 = input("Ingresa tu primer apellido\n")
apellido2 = input("Ingresa tu segundo apellido\n")
print(" ")
print("Selecciona, A: para primer nombre, B: para segundo nombre, C: para primer apellido, D: para segundo apellido\n")
seleccion = input("Ingresa A, B, C o D\n")
print(" ")
while seleccion == "A" and "B" and "C" or "D":
    if seleccion == "A":
        print("Seleccionaste " + nombre1)
        break
    elif seleccion == "B":
        print("Seleccionaste " + nombre2)
        break
    elif seleccion == "C":
        print("Seleccionaste " + apellido1)
        break
    elif seleccion == "D":
        print("Seleccionaste " + apellido2)
        break
    else:
        print("No seleccionaste nada ")


