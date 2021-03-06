from hash_structure.linkedlist import *
from hash_structure.algo1 import *
import math


class Dictionary:
	key = None
	value = None

class fileNode:
	word=None
	entry=1

#hash_function(k)=⌊m(k*A -⌊k*A⌋)⌋f
def hash_function(name, size):
	#A=0  assci-ord(A) assci>ord(A)and assci < ord(Z)  {(A=65 en ascii) (Z=90 en ascii)}
	#a=0  assci-ord(a) assci>ord(a) and assci < ord(z) {(a=97 en ascii) (z=122 en ascii)}
	word = String(name)
	word_size = len(word)
	k=0
	for i in range(0,word_size): #ord(word[i])=ascii
		assci = ord(word[i])
		if assci >= ord("A") and assci <= ord("Z"):
			k = (assci - ord("@"))*(i+1)+ k
		elif assci >= ord("a") and assci <= ord("z"):
			k = (assci - ord("`"))*(i+1) + k
		else:
			k= assci*(i+1)+ k
	## valor de A recomendado Donald Knuth
	A = (math.sqrt(5) - 1) / 2
	multi=(k*A)
	numcoma,numentero=math.modf(multi)
	key = math.floor(size * (numcoma))
	return key

# inserta un key en una posicion determinada por la funcion de hash H(K)=K mod m
def insert(dictionary, key, value, collision_counter): #O(n*t)
	long = len(dictionary)
	index = hash_function(key, long) #O(1)
	if dictionary[index] == None:
		dictionary[index] = Dictionary()
		dictionary[index].key = index
		dictionary[index].value = LinkedList()
	#revisar si existe la palabra o hay que insertar
	currentNode = dictionary[index].value.head
	auxiliar=collision_counter
	while currentNode != None: #O(n)*O(t+1)=O(n*(t+1))
		if strcmp(currentNode.value.word, value): #O(t)
			currentNode.value.entry += 1
			return collision_counter
		else:
			currentNode = currentNode.nextNode
			if collision_counter == auxiliar:
				auxiliar+=1
	#crear nuevo nodo
	newNode=fileNode()
	newNode.word=value
	#newNode.entry=1
	add(dictionary[index].value, newNode)#O(1)
	return auxiliar

# inserta un key en una posicion determinada por la funcion de hash H(K)=K mod m
def insert_nodes(dictionary, key, newNode):#O(1)
	long = len(dictionary)
	index = hash_function(key, long)#O(1)
	if dictionary[index] == None:
		dictionary[index] = Dictionary()
		dictionary[index].key = index
		dictionary[index].value = LinkedList()
	#revisar si existe la palabra o hay que insertar
	add(dictionary[index].value, newNode)#O(1)

# Busca una key, si la encuentra devuelve su value sino devuevle None
def search(dictionary, key):
	long = len(dictionary)
	index = hash_function(key, long)
	if dictionary[index] != None:
		current_chain_node = dictionary[index].value.head
		while current_chain_node != None:
			if current_chain_node.key == key:
				return current_chain_node.key
			current_chain_node = current_chain_node.next_node
		return None
	else:
		return None

	#acces
def access(D,key):
	if D[key]!=None:
		if D[key].value!=None:
			return D[key].value.head
	return None