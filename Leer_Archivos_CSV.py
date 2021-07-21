archivo = open("/Users/franciscosaraosgarcia/Documents/PYTHON/PythonVisual/Archivos_Lectura/archivo_ejemplo.csv",encoding="latin-1")
archivo_lineas = archivo.readlines()
numero_clientes = len(archivo_lineas)
matriz_datos = []
for linea in archivo_lineas:
    fila = linea.split(";")
    matriz_datos.append(fila)
print(matriz_datos)
print(" ")
for fila in matriz_datos:
    fecha_de_nacimiento = fila[3]
fecha_de_nacimiento_lista = fecha_de_nacimiento.split("/")
edad = 2018 - int(fecha_de_nacimiento_lista[0])
fila.append(edad)
print(matriz_datos)

"""archivo_guardar = open("ejemplo_con_edad.csv","w")

for fila in matriz_datos:
	fila_para_escribir = ""

	for i in range(0,len(fila)):
		if i == len(fila)-1:
			fila_para_escribir += str(fila[i])
		else:
			fila_para_escribir += fila[i] + ";"

	fila_para_escribir += "\n"

	archivo_guardar.write(fila_para_escribir)

archivo_guardar.close()"""