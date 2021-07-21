# Este codigo ha sido generado por el modulo psexport 20180802-mac de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	contrasena = str()
	contador = int()
	pas = "1234"
	print("Favor ingresar contrase�a ")
	contrasena = input()
	while pas!=contrasena:
		print("Ingresaste ",contrasena," y es incorrecta, intenta nuevamente ")
		contrasena = input()
	print("Contrase�a correcta, ingresaste al sistema ")

