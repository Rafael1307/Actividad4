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