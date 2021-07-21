# Este codigo ha sido generado por el modulo psexport 20180802-mac de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	num1 = int()
	num2 = int()
	resul = int()
	adv = int()
	enter = str()
	print(" ")
	print("SUMA DE NUMEROS PARES, SI INGRESAS UN 0 O UN NUMERO IMPAR EL PROGRAMA FINALIZA, presiona ENTER ")
	enter = input()
	print(" ")
	while True:# no hay 'repetir' en python
		print("VAMOS, Ingresa un numero PAR e inicia el sistema  ")
		advertencia = int(input())
		if (advertencia==0) or (advertencia%2==1):
			print("Ojo, no puedes ingresar un 0 o un numero IMPAR, vuelve a intentarlo  ")
		else:
			print("Excelente, ingresaste ",advertencia," y es un numero PAR, continua ")
		if (advertencia!=0) and (advertencia%2==0): break
	print(" ")
	print("RECUERDA!! RECUERDA!! RECUERDA!! - Ingresa solo numeros PARES y no 0 para sumar o el programa te sacar�. Presiona ENTER ")
	enter = input()
	while True:# no hay 'repetir' en python
		print(" ")
		print("Ingresa un numero PAR ")
		num1 = int(input())
		print("Ingresa otro numero PAR ")
		num2 = int(input())
		if (num1==0) or (num2==0) or (num1%2==1) or (num2%2==1):
			print("No se permite el 0 o numeros IMPARES para sumar. TE LO DIJEEE :D ")
		else:
			print("La suma de ",num1," y ",num2," es ",num1+num2)
		if (num1==0) or (num2==0) or (num1%2==1) or (num2%2==1): break

