from hash_structure.algo1 import *
from hash_structure.linkedlist import LinkedList, length
from hash_structure.dictionary_project import *
import os

class relevanceNode:
	relevance = None
	value = None


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
				new_path =local_path + "/" + name
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
	new_path =local_path + "/" + name
	with open(new_path, "bw") as file:
		pickle.dump(structure, file)
	#hide_file(name)


# create
def create(local_path):
	## Parte 1 (crear)
	shelf = VerdaderoCreate(local_path)

	## Parte 2 (guardar la estructura,hashTable)
	main_path = os.getcwd()
	save_structure(shelf, main_path, "estructura")
	return

# crea estructuras y coloca los pth dentro
def VerdaderoCreate(local_path):
	# creamos una linked list
	shelf = LinkedList()
	file_list = os.listdir(local_path)
	size_list = len(file_list)
	for i in range(0, size_list):
		newNode = Dictionary()
		newNode.key = file_list[i]
		file_path = local_path + "/" + file_list[i]
		newNode.value = word_indexer(file_path)
		add(shelf, newNode)
	return shelf


def word_indexer(file_path):
	array_size = 150
	book = Array(array_size, Dictionary())
	collision_counter = 0
	with open(file_path) as file:
		blank_lines = 0
		while blank_lines <= 10:
			line = file.readline()
			line = String(line)
			line_size = len(line)
			if line_size > 0:
				book=word_insert( book, line, line_size, collision_counter)
			else:
				blank_lines += 1
	return book

def word_insert(book, line, line_size, collision_counter):
	start_word = 0
	array_size = len(book)
	for i in range(0, line_size):
		if line[i] == " " or line[i] == "," or line[i] == ".":
			#substring
			end_word = i
			current_word = substr(line, start_word, end_word)
			current_word_size = len(current_word)
			start_word = end_word + 1
			#indexado de palabra
			if current_word_size != 0:
				collision_counter = insert( book, current_word, current_word, collision_counter)
			#rehashing
			if collision_counter >= array_size:
				newBook = rehashing(book)
				book = newBook
				collision_counter = 0
	return book
			
def rehashing(oldBook):
	oldBook_size = len(oldBook)
	newBook = Array(3 * oldBook_size, Dictionary())
	#recorremos oldBook
	for i in range(0, oldBook_size):
		if oldBook[i] != None:
			#insertamos todas las palanras en newBook 
			current_list_Node = oldBook[i].value.head
			while current_list_node != None:
				##insert(dictionary, key, value, collision_counter)
				insert( newBook, current_list_node.value.word, current_list_node.value, 0)
				current_list_Node = current_list_node.nextNode
	return newBook

# =====================================================================================
# =====================================================================================

# Es un contador de la cantidad de ocurrencias ocurren entre <key_word> sobre <nombre
def occurrence(fileName, key_word):
	size_key = len(key_word)
	size_name = len(fileName)
	if size_name >= size_key:
		count = 0
		key_word = String(key_word)
		fileName = String(fileName)
		# compara un substring de fileName con la key word
		for i in range(0, size_name - size_key + 1):
			if strcmp(substr(fileName, i, i + size_key), key_word):
				count = count + 1
		return count
	# si la nombre del archivo es tamaño devuleve 0
	return 0


# Imprime el array
def print_array(L):
	for i in range(0, 10):
		if L[i] != None:
			print(i + 1, "-", L[i].name)
			print("   ", L[i].path)
			print("")
		else:
			return


# Hace que la lista ingresada se simplifique en un array y que se ordene de mayor a menor segun la relevancia(key)
def order(L):
	own_list = Array(10, fileNode())
	if L.head != None:

		for i in range(0, 10):
			referenceNode = L.head
			if referenceNode==None:
				break
			currentNode = L.head.nextNode
			if currentNode != None:
				while currentNode != None:
					if referenceNode.value.relevance < currentNode.value.relevance:
						referenceNode = currentNode
					currentNode=currentNode.nextNode
			# crear el fileNode para un array
			own_list[i] = fileNode()
			own_list[i].path = referenceNode.value.value.path
			own_list[i].name = referenceNode.value.value.name
			delete_by_node(L, referenceNode)
		return print_array(own_list)
	else:
		print("no document found")


# Busca en otra hash table (en una sub-carpeta)
def search_folder(L, hash_path, key_word):
	hash = load_structure(hash_path, "estructura")
	for i in range(0, len(hash)):

		if hash[i] != None:
			hashSlot = hash[i].value.head
			while hashSlot != None:
				nodoArchivo = hashSlot.value
				if nodoArchivo.isFolder:
					search_folder(L, nodoArchivo.path, key_word)
				else:
					relevance = occurrence(nodoArchivo.name, key_word)
					# se filtran todos los archivos sin relacion(relevance==0)
					if relevance > 0:
						newNode = relevanceNode()
						newNode.relevance = relevance
						newNode.value = hashSlot.value
						add(L, newNode)
				hashSlot = hashSlot.nextNode
	return L


# Devuleve una lista de archivos con prioridad por aparicion de key_word en el nombre
def search(key_word):
	main_path = os.getcwd()
	file_lists = os.listdir(main_path)
	existe = False
	for i in range(0, len(file_lists)):
		if file_lists[i] == "directorios_raiz":
			existe = True
			break
	if existe == True:
		lista_raiz = load_structure(main_path, "directorios_raiz")
		L = LinkedList()
		currentNode = lista_raiz.head
		while currentNode != None:
			search_folder(L, currentNode.value, key_word)
			currentNode = currentNode.nextNode
		order(L)
	else:
		print("No se ha creado ningun directorio previamente en el cual buscar.")

"""
# =========================FUNCIONA EN WINDOWS===========================================
# Eso depende del sistema operativo que se utiliza. En las ventanas hay un Hiddensistema de archivos de atributo se puede establecer en los archivos:
def hide_file(filename):
	import win32file
	import win32con
	import win32api
	flags = win32file.GetFileAttributesW(filename)
	win32file.SetFileAttributes(filename, win32con.FILE_ATTRIBUTE_HIDDEN | flags)
# ==========================FUNCIONA EN LINUX==========================================
# En Unix / Linux los archivos ocultos son los que empiezan por un punto ."" Usted sólo puede cambiar el nombre del archivo:
def hide_file(filename):
    import os
    os.rename(filename, os.path.join(os.path.dirname(filename), '.' + os.path.basename(filename)))
"""