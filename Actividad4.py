def cuadrado(a):
	return a*a
	
def triangulo(a, b):
	return (a*b)/2
	
def circulo(a):
	return 3.1416*(a*a)
	
def operaciones():
	print("Elige una opcion para sacr area")
	print("1) Cuadrado")
	print("2) Triangulo")
	print("3) Circulo")
	op = input()
	if op == "1":
		print("Area: ", cuadrado(int(input("medida de lado: "))))
	elif op == "2":
		print("Area: ", triangulo(int(input("base: ")), int(input("altura: "))))
	elif op == "3":
		print("Area: ", circulo(int(input("medida de radio: "))))
	else:
		print("Opcion invalida")
	return 0

def signos():
	mes = input("Ingresa tu mes de nacimiento: ")
	dia = int(input("Ingresa tu dia de nacimiento: "))
	if mes == "enero":
		if dia > 0 and dia <= 20:
			print("Tu signo es Capricornio")
		elif dia > 20 and dia <= 31:
			print("Tu signo es Acuario")
		else:
			print("Dia incorrecto")
	elif mes == "febrero":
		if dia > 0 and dia <= 19:
			print("Tu signo es Acuario")
		elif dia > 19 and dia <= 31:
			print("Tu signo es Piscis")
		else:
			print("Dia incorrecto")
	elif mes == "marzo":
		if dia > 0 and dia <= 20:
			print("Tu signo es Piscis")
		elif dia > 20 and dia <= 31:
			print("Tu signo es Aries")
		else:
			print("Dia incorrecto")
	elif mes == "abril":
		if dia > 0 and dia <= 20:
			print("Tu signo es Aries")
		elif dia > 20 and dia <= 31:
			print("Tu signo es Tauro")
		else:
			print("Dia incorrecto")
	elif mes == "mayo":
		if dia > 0 and dia <= 20:
			print("Tu signo es Tauro")
		elif dia > 20 and dia <= 31:
			print("Tu signo es Geminis")
		else:
			print("Dia incorrecto")
	elif mes == "junio":
		if dia > 0 and dia <= 2:
			print("Tu signo es Geminis")
		elif dia > 21 and dia <= 31:
			print("Tu signo es Cancer")
		else:
			print("Dia incorrecto")
	elif mes == "julio":
		if dia > 0 and dia <= 22:
			print("Tu signo es Cancer")
		elif dia > 22 and dia <= 31:
			print("Tu signo es Leo")
		else:
			print("Dia incorrecto")
	elif mes == "agosto":
		if dia > 0 and dia <= 23:
			print("Tu signo es Leo")
		elif dia > 23 and dia <= 31:
			print("Tu signo es Virgo")
		else:
			print("Dia incorrecto")
	elif mes == "septiembre":
		if dia > 0 and dia <= 22:
			print("Tu signo es Virgo")
		elif dia > 22 and dia <= 31:
			print("Tu signo es Libra")
		else:
			print("Dia incorrecto")
	elif mes == "octubre":
		if dia > 0 and dia <= 22:
			print("Tu signo es Cancer")
		elif dia > 22 and dia <= 31:
			print("Tu signo es Leo")
		else:
			print("Dia incorrecto")
	elif mes == "noviembre":
		if dia > 0 and dia <= 22:
			print("Tu signo es Leo")
		elif dia > 22 and dia <= 31:
			print("Tu signo es Virgo")
		else:
			print("Dia incorrecto")
	elif mes == "diciembre":
		if dia > 0 and dia <= 21:
			print("Tu signo es Virgo")
		elif dia > 21 and dia <= 31:
			print("Tu signo es Libra")
		else:
			print("Dia incorrecto")
	else:
		print("Mes incorrecto")
	return 0