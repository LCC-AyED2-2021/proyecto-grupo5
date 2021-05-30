from hash_structure.algo1 import *


class LinkedList:
	head = None


class Node:
	value = None
	nextNode = None


# Agrega un elemento al comienzo de L, siendo L una LinkedList que representa el TAD secuencia.
def add(L, element):
	newNode = Node()
	# aqui coloco el Nodo de head como siguiente nodo del new node
	newNode.nextNode = L.head
	newNode.value = element
	L.head = newNode
	return


# Busca un elemento de la lista que representa el TAD secuencia.
def search(L, element):
	currentNode = L.head
	position = 0
	# recorro toda la lista hasta encontrar el elemnto
	while currentNode != None:
		if currentNode.value == element:
			return position
		else:
			position = position + 1
		currentNode = currentNode.nextNode
	# si no encuentra el elemento retorna None
	return None


# Agrega un elemento al final de L, siendo L una LinkedList que representa el TAD secuencia.
def lastInsert(L, element):
	newNode = Node()
	newNode.value = element
	if L == None:
		L = LinkedList()
	if L.head != None:
		currentNode = L.head
		while currentNode.nextNode != None:
			currentNode = currentNode.nextNode
		# aqui coloco el Nodo de head como siguiente nodo del new node
		currentNode.nextNode = newNode
	else:
		L.head = newNode


# Inserta un elemento en una posición determinada de la lista que representa el TAD secuencia.
def insert(L, element, position):
	# verifica que la lista no este vacia
	if L.head == None:
		# si esta vacia, comprueba si la psicion es 0
		if position == 0:
			add(L, element)
			return position
		else:
			# si la psocion no es 0 entonces no lo inserta
			return None
	else:
		# No esta vacia
		currentNode = L.head
		# chekeamos si la posicion anterior existe
		existe = checkNode(L, position)
		if existe == True:
			newNode = Node()
			# se crea un nuevo nodo
			for i in range(0, position):
				if i == position - 1:
					# se llena el nodo nuevo y se linkea al anterior
					newNode.value = element
					newNode.nextNode = currentNode.nextNode
					currentNode.nextNode = newNode
				else:
					currentNode = currentNode.nextNode
			return position
		else:
			# si la posicion anterior no existe, no se puede insertar
			return None


# elimina un nodo de una lista
def delete_by_node(L, Node):
	currentNode = L.head
	if currentNode==Node:
		L.head=currentNode.nextNode
		return Node.value

	while currentNode.nextNode != None:
		if currentNode.nextNode == Node:
			currentNode.nextNode= currentNode.nextNode.nextNode
			return Node.value
		currentNode = currentNode.nextNode
	return None


# Elimina un elemento de la lista que representa el TAD secuencia.
def delete(L, element):
	# busco el elemento en la lista
	position = search(L, element)
	# lista vacia?
	if L.head != None and position != 0:
		currentNode = L.head
		for i in range(0, position):
			# si la posicion actual es la anterior a la ingresada
			if i == position - 1:
				# se linkea el anterior al siguiente.
				currentNode.nextNode = currentNode.nextNode.nextNode
				return position
			else:
				# si no es se sigue recorriendo
				currentNode = currentNode.nextNode
	else:
		# si la lista tiene un elemento en 0
		if position == 0:
			L.head = L.head.nextNode
	return None


# Calcula el número de elementos de la lista que representa el TAD secuencia .
def length(L):
	# si esta vacia retorna 0
	if L.head == None:
		return 0
	else:
		# se cuentan los nodos
		currentNode = L.head
		long = 0
		while currentNode != None:
			long = long + 1
			currentNode = currentNode.nextNode
		return long


# Permite acceder a un elemento de la lista en una posición determinada.
def access(L, position):
	currentNode = L.head
	# si no esta vacia la lista
	if L.head != None:
		currentNode = L.head
		# se recorre la lista hasta
		if position == 0:
			return L.head.value
		else:
			for i in range(0, position):
				# se busca el nodo anterior para acceder al siguiente
				if i == (position - 1):
					element = currentNode.nextNode.value
					return element
				else:
					currentNode = currentNode.nextNode
	return None


# Permite cambiar el valor de un elemento de la lista en una posición determinada.
def update(L, element, position):
	# se busca si existe el anterior
	existe = checkNode(L, position)
	currentNode = L.head
	if existe == True:
		# se recorre hasta el anterior de la posicion
		for i in range(0, position):
			currentNode = currentNode.nextNode
		# cuando se llega, se le asigna el valor al siguiente nodo
		currentNode.value = element
		return position
	else:
		return None


# printlist con nodos en el campo value
def printlist_node(l):
	currentNode = l.head
	while currentNode != None:
		print(currentNode.value.key, end="")
		if currentNode.nextNode != None:
			print(",", end="")
		currentNode = currentNode.nextNode
	print()


# entrad:la lista,Salida:la lista en consola
def printlist(A):
	currentNode = A.head
	while currentNode != None:
		# if currentNode.value != None:
		print(currentNode.value, end=",")
		currentNode = currentNode.nextNode
	print()
	return


# Busca si el existe un nodo en la posicion ingresada
def checkNode(L, position):
	currentPosition = 0
	currentNode = L.head
	existe = False
	i = 0
	# se recorre toda la lista hasta el anterior nodo que se ingreso
	while i != -1:
		# revisa si el nodo anterior existe
		if currentPosition == (position - 1):
			existe = True
			# si existe, se puede colocar el nodo en la psocion ingresada
			return existe
		if currentNode.nextNode != None:
			i = i + 1
		else:
			i = -1
		currentPosition = currentPosition + 1
		currentNode = currentNode.nextNode
	return existe