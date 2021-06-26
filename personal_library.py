from hash_structure.algo1 import *
from hash_structure.linkedlist import LinkedList, add, insert_ordenado, length
from hash_structure.dictionary_project import *
import os
import sys

# =========================CLASES======================================================
# =====================================================================================
class relevanceNode:
	relevance = None
	book = None


# ==========================PERSISTENCIA DE DATOS======================================
# =====================================================================================

# carga en un archivo "estructura" el hash del directorio que se accede.
def load_structure(local_path, name):
	# Hace una lista con todos los archivos que hay en la carpeta local_path.
	file_lists = os.listdir(local_path)
	# Si la lista no esta vacia, importa pickle.
	if file_lists != []:
		import pickle
		longitud = len(file_lists)
		for i in range(0, longitud):
			# si se encuentra el Archivo con el nombre buscado.
			if file_lists[i] == name:
				# open no permite usar STRING DE ALGO1(NO permite arreglos)
				new_path = local_path + "/" + name
				# abrimos el archivo en forma de escritura binaria.
				with open(new_path, "br") as file:
					# se carga del archivo la estructura que se devuelve.
					structure = pickle.load(file)
					return structure
	return None


# guarda la estructura que hayan creado en  un archivo "estructura" se guarda en el directorio que se ha creado
def save_structure(structure, local_path, name):
	import pickle
	##abre el archivo "estructura" en modo binary_write y comprime la estructura hash
	# open no permite usar STRING DE ALGO1(NO permite arreglos)
	new_path = local_path + "/" + name
	sys.setrecursionlimit(10000)
	with open(new_path, "bw") as file:
		pickle.dump(structure, file)#O(structure)
	print()


# hide_file(name)

# ===================================CREATE============================================
# =====================================================================================

# create
def create(local_path): #O(L^4*S); L cantidad de caracteres linea con mas caracteres; S cantidad de slots del hash mas grande
	## Parte 1 (crear)
	shelf = VerdaderoCreate(local_path) #O(L^4*S)

	## Parte 2 (guardar la estructura,hashTable)
	main_path = os.getcwd()
	save_structure(shelf, main_path, "estructura") #O(structure)
	print("Library created successfully.")
	return


# crea estructuras y coloca los path dentro
def VerdaderoCreate(local_path):#O(L^4*S)
	# creamos una linked list
	shelf = LinkedList()
	file_list = os.listdir(local_path)
	size_list = len(file_list)
	for i in range(0, size_list): #O(J)=O(L)*O(L^3*S); J=cantidad de archivos
		newNode = Dictionary()
		newNode.key = file_list[i]
		file_path = local_path + "/" + file_list[i] #O(1)
		newNode.value = word_indexer(file_path) #O(L^3*S)
		add(shelf, newNode)#O(1)
	return shelf


def word_indexer(file_path):#O(L^3*S)
	array_size = 150
	book = Array(array_size, Dictionary())
	collision_counter = 0
	with open(file_path,encoding="utf-8") as file:
		blank_lines = 0
		while blank_lines <= 10: #O(N)=O(L)*O(L^2*S);N=cantidad de lineas del texto por archivo
			line = file.readline()
			line = String(line)
			line_size = len(line)
			if line_size > 0:
				tupla=word_insert(book, line, line_size, collision_counter) #O(L^2*S)
				book=tupla[0]
				collision_counter=tupla[1]
			else:
				blank_lines += 1
	return book

def char_verifier(char):
	#ignora los caracteres "'","_"
	if char=="\n":
		return True
	ascci=ord(char)
	if ascci>=ord(" ") and ascci<= ord("/") :
		return True
	elif  ascci>=ord(":") and ascci<= ord("?"):
		return True
	elif ascci>=ord("[") and ascci<= ord("^"):
		return True
	elif ascci >= ord("{") and ascci <= ord("~"):
		return True
	return False


def word_insert(book, line, line_size, collision_counter):
	# O((L^2)*(1+S+(S^2/L)) = L^2 + S*L^2 + L*S^2 = O(L^2*S) <- O(L*M(1+K*(1+S/M)) S es la cantidad de slot del hash actual;L es la cantidad de letras por linea
	start_word = 0
	array_size = len(book)
	for i in range(0, line_size): #O(L);L es la cantidad de letras por linea
		if char_verifier(line[i]) or i==(line_size-1):
			# se realiza un substring en la linea para sacar una palabra
			end_word = i
			current_word = substr(line, start_word, end_word) #O(M=L/2);M es tamaño de cada palabra de una linea
			current_word_size = len(current_word)
			start_word = end_word + 1
			# indexado de palabra
			if current_word_size != 0:
				collision_counter = insert(book, current_word, current_word, collision_counter) #O(K*M);K es el tamaño la lista que hay en cada slot
			# rehashing
			if collision_counter >= array_size:
				newBook = rehashing(book) #O(S*K=2*S)=O(S^2);S es la cantidad de slot del hash actual
				book = newBook
				collision_counter = 0
	return book,collision_counter


def rehashing(oldBook):#O(S*K=2*S)=O(S^2);L cantidad de caracteres linea con mas caracteres; S cantidad de slots del hash mas grande
	oldBook_size = len(oldBook)
	newBook = Array(3 * oldBook_size, Dictionary())
	# recorremos oldBook
	for i in range(0, oldBook_size):#O(S)*O(K);K es el tamaño la lista que hay en cada slot
		if oldBook[i] != None:
			# insertamos todas las palanras en newBook
			current_list_Node = oldBook[i].value.head
			while current_list_Node != None:#O(L)
				##insert(dictionary, key, value, collision_counter)
				insert_nodes(newBook, current_list_Node.value.word, current_list_Node.value)#O(1)
				current_list_Node = current_list_Node.nextNode
	return newBook


# ====================================SEARCH===========================================
# =====================================================================================


# imprime una lista de nodos relevanceNode con un indice
def printList(L): #O(K); tamaño de la lista por slot
	currentNode = L.head
	i = 1
	while currentNode != None:
		print(i, ".", currentNode.value.book, " ", currentNode.value.relevance)
		i += 1
		currentNode = currentNode.nextNode


# revisa el slot donde esta deberia estar almacenada la palabra, si la encuentra la agrega a la lista L
def search_in_book(D, L, key_word, book_name):#O(2*S^2*L)=O(S^2*L)
	key = hash_function(key_word, len(D))
	currentNode = access(D, key)
	if currentNode == None:
		return
	# se revisa la lista del slot
	while currentNode != None:#O(K*K*M)=O(K^2*M) K=2*S M= L/2
		if strcmp(currentNode.value.word, key_word):#O(M) tamaño de alguna plabra de una linea
			newNode = relevanceNode()
			newNode.book = book_name
			newNode.relevance = currentNode.value.entry
			insert_ordenado(L, newNode)#O(K); tamaño de la lista por slot
			return L
		currentNode = currentNode.nextNode
	return


# Devuleve una lista de archivos con prioridad por aparicion de key_word en el nombre
def search(key_word):#O(L)*O(S^2*L)+O(S)= O(S^2*L^2)
	word = String(key_word)
	main_path = os.getcwd()
	shelf = load_structure(main_path, "estructura")
	if shelf != None:
		currentNode = shelf.head
		words_list = LinkedList()
		# buscamos en hash por hash en su slot correspondiente
		while currentNode != None:#O(J)=O(L) ;J cantidad de archivos
			D = currentNode.value.value
			search_in_book(D, words_list, word, currentNode.value.key);#O(S^2*L)
			currentNode = currentNode.nextNode

		if words_list.head != None:
			print("Results from the search of","'",key_word,"'")
			printList(words_list)#O(K)=O(S); tamaño de la lista por slot
		else:
			print("No document found.")
	else:
		print("No document found.")