from hash_structure.algo1 import *
from hash_structure.linkedlist import LinkedList, length
from hash_structure.Proyecto_dictionary import *
import os


class fileNode:
	name = None
	path = None
	isFolder = None


class relevanceNode:
	relevance = None
	value = None


# carga en un archivo "estructura" el hash del directorio que se accede.
def load_structure(local_path, name):
	# Hace una lista con todos los archivos que hay en la carpeta local_path.
	lista_archivos = os.listdir(local_path)
	# Si la lista no esta vacia, importa pickle.
	if lista_archivos != []:
		import pickle
		longitud = len(lista_archivos)
		for i in range(0, longitud):
			# si se encuentra el Archivo con el nombre buscado.
			if lista_archivos[i] == name:
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
	## Parte 1(cargar estructura, hashTable)
	# esta funcion me devuelve una variable (mi hash table)
	hashTable = load_structure(local_path, "estructura")

	## Parte 2 (crear)
	hashTable = VerdaderoCreate(hashTable, local_path)

	## Parte 3 (guardar la estructura,hashTable)
	save_structure(hashTable, local_path, "estructura")
	return


# opcion ecrear carpeta o crear
def elegirOpcion():
	option = 0
	while option != "1" and option != "2":
		print("1.crear archivo")
		print("2.crear nueva carpeta")
		option = input("")
	return option


# pide el nombre del archivo por teclado
def newFileName():
	fileName = input("Inserte el nombre del archivo: ")
	return fileName


# crea estructuras y coloca los pth dentro
def VerdaderoCreate(hash, local_path):
	option = elegirOpcion()

	# creamos un archivo
	if hash == None:
		# crear una estructura hash
		hash = Array(50, dictionary())
		# guarda el path en una lista
		Raices = LinkedList()
		add(Raices, local_path)
		main_path = os.getcwd()
		# main_path="D:\Documentos de Usuario\Desktop\carpeta pruebas"
		save_structure(Raices, main_path, "directorios_raiz")

	nameFile = newFileName()
	if option == "1":
		# crear nuevo nodo archivo
		newNode = fileNode()
		newNode.name = nameFile
		newNode.path = local_path
		newNode.isFolder = False
		# se inserta el nodo en el diccionario
		hash = insert(hash, nameFile, newNode)
		# creamos el nuevo path
		#open no permite usar STRING DE ALGO1(NO permite arreglos)
		path=local_path + "/" + nameFile + ".txt"
		# se verifica si podemos abrir el archivo
		with open(path, "w") as newFile:
			print("library created successfully")

	elif option == "2":
		# open no permite usar STRING DE ALGO1(NO permite arreglos)
		local_new_path= local_path + "/" + nameFile
		new_directory = os.mkdir(local_new_path)
		# crear nuevo nodo carpeta
		newNode = fileNode()
		newNode.name = nameFile
		newNode.path = local_new_path
		newNode.isFolder = True
		insert(hash, nameFile, newNode)
		folder = Array(50, dictionary())
		save_structure(folder, local_new_path, "estructura")
		print("library created successfully")

	return hash


# =====================================================================================
# =====================================================================================

# Es un contador de la cantidad de ocurrencias ocurren entre <key_word> sobre <nombre
def occurrence(nombreArchivo, key_word):
	size_key = len(key_word)
	size_name = len(nombreArchivo)
	if size_name >= size_key:
		count = 0
		key_word = String(key_word)
		nombreArchivo = String(nombreArchivo)
		# compara un substring de nombreArchivo con la key word
		for i in range(0, size_name - size_key + 1):
			if strcmp(substr(nombreArchivo, i, i + size_key), key_word):
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
	lista_archivos = os.listdir(main_path)
	existe = False
	for i in range(0, len(lista_archivos)):
		if lista_archivos[i] == "directorios_raiz":
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