# Paquete algo1.py
# jue oct 12 13:26:46 ART 2017
# Algoritmos y Estructuaras de datos I
# Funciones de carga de valores
import copy


def input_int(str):
	try:
		ingreso = int(float(input(str)))
	except:
		ingreso = 0
	return ingreso


def input_real(str):
	try:
		ingreso = float(input(str))
	except:
		ingreso = 0.0
	return ingreso


def input_str(str):
	try:
		ingreso = input(str)
	except:
		ingreso = ""
	return ingreso


# Clase arreglos
class Array:
	data = []

	def __init__(self, size=None, init_value=0):
		if size == None:
			self.size = 0
		else:
			self.size = size
		if type(init_value) != Array:
			self.data = [copy.deepcopy(None) for i in range(0, size)]
		else:
			self.data = [copy.deepcopy(init_value) for i in range(0, size)]
		self.type = type(init_value)

	def __getitem__(self, index):
		if index > self.size:
			print("IndexError: index Out of bounds")
		else:
			return self.data[index]

	def __setitem__(self, index, value):
		if index > self.size:
			print("IndexError: index Out of bounds")
		elif type(value) != self.type and value != None:
			print("TypeError: value error")
		else:
			self.data[index] = value

	def __str__(self):
		return str([self.data[i] for i in range(0, len(self.data))])

	def __len__(self):
		return (self.size)


class String:
	def __init__(self, string):
		self.arr = Array(len(string), 'c')
		self.arr.data = string

	def __getitem__(self, index):
		return self.arr[index]

	def __setitem__(self, index, value):
		self.arr[index] = value

	def __str__(self):
		return str(self.arr.data)

	def __len__(self):
		return len(self.arr)


def substr(t, start, end):
	return String(''.join([t[i] for i in range(start, end)]))


#mi funcion, cmabia todos los caracteres a minusculas
def capital(caracter):
	ascci=ord(caracter)
	if ascci >= ord("A") and ascci <= ord("Z"):
		newchr=chr(ascci+32)
		return newchr
	else:
		return caracter

# O(t+1). Donde t es la cantidad de caracteres que matchearon y 1 es para el caso de t=0
def strcmp(t, p):
	#agregamos esta linea
	if len(t)==len(p):
		for i in range(0, len(p)):
			#no distingue entre mayusculas y minusculas
			if capital(t[i]) != capital(p[i]):
				return False
		return True
	return False

def concat(s, c):
	return String(s.arr.data + c.arr.data)