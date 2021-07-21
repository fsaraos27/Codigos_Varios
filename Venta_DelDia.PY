print("")

costo_zapatilla = 30000
valor_pagar = 0
total_venta_jornada = 0
clientes = 0
zapatillas = 0
dia_laboral = 8
recaudacxion = 0
cont = 1

cantidad_clientes = int(input("¿ Cuantos clientes hay en la tienda ?\n"))

while cont <= cantidad_clientes:
    num1 = int(input("¿ Cuantas zapatillas lleva ?\n"))
    total = costo_zapatilla * num1
    if num1 < 3:
        print("No hay descuento! total a pagar: ", total)

        clientes = clientes + 1
        zapatillas = num1 + clientes
        valor_pagar = zapatillas * costo_zapatilla
        recaudacion = valor_pagar * cantidad_clientes * dia_laboral
        cont = cont + 1
    
    elif num1 >= 3 and num1 < 10:
        print("Tiene descuento del 20%, Total a pagar: ", total * 0.20)

        clientes = clientes + 1
        zapatillas = num1 + clientes
        valor_pagar = zapatillas * costo_zapatilla
        recaudacion = valor_pagar * cantidad_clientes * dia_laboral
        cont = cont + 1

    elif num1 > 10:
        print("Tiene un 30% de descuento, total a pagar: ", total * 0.30)

        clientes = clientes + 1
        zapatillas = num1 + clientes
        valor_pagar = zapatillas * costo_zapatilla
        recaudacion = valor_pagar * cantidad_clientes * dia_laboral
        cont = cont + 1
    

        

print("")

print("Clientes atendidos: ", clientes)
print("Total de Zapatillas: ", zapatillas)
print("Venta Total: ", valor_pagar)
print("Recaudacion del dia: ", recaudacion)

print("")



""" elif num1 >= 3 or num1 <= 10:
        print("Tiene descuento del 20%, Total a pagar: ", total * 0.20)

    elif num1 >= 10:
        print("Tiene un 30% de descuento, total a pagar: ", total * 0.30) """