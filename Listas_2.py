print(" ")
input("Presiona enter para mostrar la lista\n")
lista1 = ["admin", "rrhh", "conta"]
print(lista1)
print(" ")
input("Presiona enter para cambiar el elemento\n")
lista1 [2] = "infra"
print(lista1)
print(" ")
print("Cambiaste conta por", lista1[2])
print(" ")
input("Presiona enter para agregar un elemnto\n")
lista1.append("marke")
print("Agregaste", lista1[3], "a la lista ")
print(" ")
print(lista1)
print(" ")
input("Presiona enter para remover un elemento\n")
lista1.remove("rrhh")
print("Removiste rrhh de la lista ")
print(" ")
print(lista1)
print(" ")
input("Presiona enter para agregar elementos\n")
lista2 = "diseño" , "desarrollo"
lista1.extend(lista2)
print("Se han agregado ", lista2, "a la lista")
print(" ")
print(lista1)
print(" ")
input("Presiona enter para contar elementos\n")
print("La lista", lista1, "tiene", lista1.count("desarrollo"), "desarrollo ")
print(" ")
input("Presiona enter para mostrar el indice de un elemento de la lista\n")
print("El elemento seleccionado ", lista1[3], "perteneciente a la lista, está en el indice numero", lista1.index("diseño"))
print(" ")
input("Presiona enter para ordenar la lista\n")
print("La lista ", lista1, "Se reordenara de la siguiente manera ")
lista1.sort()
print(" ")
print("El nuevo orden de la lista es ", lista1)
print(" ")
input("Presiona enter para recorrer la lista\n")
for i in lista1:
    print(i)
print(" ")
input("Presiona enter para ingresar los colaboradores la lista\n")
nombres = input("Ingrese los nombres de los colaboradores\n")
print(" ")
print("Los colaboradores de la lista, pertenecientes a ", lista1, "son los siguientes ", nombres)
print(" ")
input("Presione enter para agregar los nombre a una lista\n")
print("los colaboradores ingresados se agregaron a la siguiente lista ", nombres.split(","))
print(" ")
input("Presiona enter para mostrar el primer nombre de la lista\n")
print(nombres[0])
