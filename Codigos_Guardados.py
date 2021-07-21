print(len(matriz_datos))
print(len(matriz_datos[0]))
print(" ")
for fila in matriz_datos:
    fila[7] = fila[7].strip()
print(matriz_datos)
print(" ")
for fila in matriz_datos:
    valor_cliente = fila[4]
    fila[4] = valor_cliente[len(valor_cliente)-1]
print(matriz_datos



# calcula edad
for i in matriz_datos:
    fecha_con_anio = i[3]
    lista_fecha = fecha_con_anio.split('/')
    edad = 2021 - int(lista_fecha[0])
    i[4] = edad
 
#limpia puntaje crediticio
for i in matriz_datos:
    puntaje = i[7]
    i[7] = puntaje.strip('\n')

print(matriz_datos)


