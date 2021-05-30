from hash_structure.linkedlist import *
from hash_structure.algo1 import *
import math


class dictionary:
	key = None
	value = None

# hash_function(k)=⌊m(k*A -⌊k*A⌋)⌋
def hash_function(name, size):
	k = ord(name[0])
	## valor de A recomendado Donald Knuth
	A = (math.sqrt(5) - 1) / 2
	key = math.floor(size * ((k * A) - math.floor(k * A)))
	return key

# inserta un key en una posicion determinada por la funcion de hash H(K)=K mod m
def insert(Dictionary, key, value):
	long = len(Dictionary)
	index = hash_function(key, long)
	if Dictionary[index] == None:
		Dictionary[index] = dictionary()
		Dictionary[index].key = index
		Dictionary[index].value = LinkedList()
	add(Dictionary[index].value, value)
	return Dictionary

# Busca una key, si la encuentra devuelve su value sino devuevle None
def search(Dictionary, key):
	long = len(Dictionary)
	index = hash_function(key, long)
	if Dictionary[index] != None:
		currentChainNode = Dictionary[index].value.head
		while currentChainNode != None:
			if currentChainNode.key == key:
				return currentChainNode.key
			currentChainNode = currentChainNode.nextNode
		return None
	else:
		return None