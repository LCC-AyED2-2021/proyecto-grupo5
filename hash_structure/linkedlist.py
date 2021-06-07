from hash_structure.algo1 import *


class LinkedList:
	head = None


class Node:
	value = None
	nextNode = None


# Agrega un elemento al comienzo de L, siendo L una LinkedList que representa el TAD secuencia.
def add(L, element):
	newNode = Node()
	newNode.nextNode = L.head
	newNode.value = element
	L.head = newNode
	return


# Inserta un elemento en una posición determinada de la lista que representa el TAD secuencia.
def insert(L, element, position):
	if L.head == None:
		if position == 0:
			add(L, element)
			return position
			return None
	else:
		currentNode = L.head
		exist = check_node(L, position)
		if exist == True:
			newNode = Node()
			for i in range(0, position):
				if i == position - 1:
					newNode.value = element
					newNode.nextNode = currentNode.nextNode
					currentNode.nextNode = newNode
				else:
					currentNode = currentNode.nextNode
			return position
		else:
			return None


# elimina un nodo de una lista
def delete_by_node(L, Node):
	currentNode = L.head
	while currentNode.nextNode != None:
		if currentNode.nextNode == Node:
			currentNode.nextNode = currentNode.nextNode.nextNode
			return Node.value
		currentNode = currentNode.nextNode
	return None


# Calcula el número de elementos de la lista que representa el TAD secuencia .
def length(L):
	if L.head == None:
		return 0
	else:
		currentNode = L.head
		long = 0
		while currentNode != None:
			long = long + 1
			currentNode = currentNode.nextNode
		return long


# Busca si el existe un nodo en la posicion ingresada
def check_node(L, position):
    current_position = 0
    currentNode = L.head
    exist = False
    i = 0
    
    while i != -1:
        # revisa si el nodo anterior existe
        if current_position == (position - 1):
            exist = True
            # si existe, se puede colocar el nodo en la psocion ingresada
            return exist
        if currentNode.nextNode != None:
            i = i + 1
        else:
            i = -1
        current_position = current_position + 1
        currentNode = currentNode.nextNode
    return exist
