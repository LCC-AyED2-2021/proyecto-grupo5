from hash_structure.algo1 import *
from hash_structure.linkedlist import LinkedList,length
from hash_structure.Proyecto_dictionary import *
import os

class fileNode:
     name=None
     path=None
     isFolder=None

class relevanceNode:
    relevance=None
    value=None

# carga en un archivo "estructura" el hash del directorio que se accede
def load_structure(local_path, name):
    ## hace una lista con todos los archivos que hay en la carpeta local_path
    lista_archivos = os.listdir(local_path)
    ## si la lista no esta vacia, importa pickle(sirve para agarrar una estructura, convertirla en binario y noseque mas)
    if lista_archivos != []:
        import pickle
        longitud = len(lista_archivos)
        for i in range(0, longitud):
            ## el archivo estructura tiene codificado en binario el Hash para poder poder buscar dentro de archivos
            ## y carpetas
            if lista_archivos[i] == name:
                ## esta funcion toma el archivo estructura y lo "abre" para poder escribirlo en binario.
                ## br-> binary_read(basicamente lo que hace es poder leer el archivo)
                new_path=local_path + "/" + name
                with open(new_path, "br") as file:
                    ## pickle.load -> esta funcion descomprime el archivo file(contiene "estructura adentro pasado a binario") y lo manda a un archivo hash
                    structure = pickle.load(file)
                    return structure
    ## retorna hash que será mi hashtTable
    return None


# guarda la estructura que hayan creado en  un archivo "estructura" se guarda en el directorio que se ha creado
def save_structure(structure, local_path, name):
    import pickle
    ##abre el archivo "estructura" en modo binary_write y comprime la estructura hash
    with open(local_path + "/" + name, "bw") as file:
        pickle.dump(structure, file)



# create
def create(local_path):
    ## Parte 1(cargar estructura, hashTable)
    # esta funcion me devuelve una variable (mi hash table)
    hashTable = load_structure(local_path,"estructura")

    ## Parte 2 (crear)
    hashTable=VerdaderoCreate(hashTable, local_path)

    ## Parte 3 (guardar la estructura,hashTable)
    save_structure(hashTable, local_path,"estructura")
    return


# opcion ecrear carpeta o crear
def elegirOpcion():
    option = 0
    while option != "1" and option != "2":
        print("1.crear archivo")
        print("2.crear nueva carpeta")
        option = input("")
    return option


def newFileName():
    fileName = input("Inserte el nombre del archivo: ")
    return fileName


def VerdaderoCreate(hash, local_path):
    option = elegirOpcion()

    # creamos un archivo
    if hash == None:
        # crear una estructura hash
        hash = Array(50, dictionary())
        #guarda el path en una lista
        Raices=LinkedList()
        add(Raices,local_path)
        main_path = os.getcwd()
        #main_path="D:\Documentos de Usuario\Desktop\carpeta pruebas"
        save_structure(Raices,main_path,"directorios_raiz")

    nameFile = newFileName()
    if option == "1":
        # crear nuevo nodo archivo
        newNode=fileNode()
        newNode.name=nameFile
        newNode.path=local_path
        newNode.isFolder=False
        hash=insert(hash, nameFile, newNode)
        path = local_path + "/" + nameFile + ".txt"
        with open(path, "w") as newFile:
            print("Se creo el archivo correctamente")

    elif option == "2":
        local_new_path = local_path + "/" + nameFile
        new_directory = os.mkdir(local_new_path)
        #crear nuevo nodo carpeta
        newNode = fileNode()
        newNode.name = nameFile
        newNode.path=local_new_path
        newNode.isFolder=True
        insert(hash, nameFile, newNode)
        folder = Array(50, dictionary())
        save_structure(folder, local_new_path, "estructura")
        print("Se creo la carpeta correctamente")

    return hash


# =====================================================================================
# =====================================================================================

# Es un contador de la cantidad de ocurrencias ocurren entre <key_word> sobre <nombre
def occurrence(nombreArchivo, key_word):
    t = len(key_word)
    s = len(nombreArchivo)
    if s >= t:
        count = 0
        for i in range(0, s - t + 1):
            if str(substr(nombreArchivo, i, i + t)) == str(key_word):
                count = count + 1

        return count

    return 0


def print_array(L):
    for i in range(0, 10):
        if L[i] != None:
            print(i+1, "-", L[i].name)
            print("   ", L[i].path)
            print("")
        else:
            return


# hace que la lista ingresada se simplifique en un array y que se ordene de mayor a menor segun la relevancia(key)
def order(L):
    list = Array(10, fileNode())
    if L.head != None:
        i=0
        while i<=9:
            currentNode = L.head
            nextNode = L.head.nextNode
            if nextNode!=None:
                while currentNode!=None:
                    if currentNode.value.relevance > nextNode.value.relevance:
                        currentNode = nextNode
                    currentNode=nextNode
            #crear el fileNode para un array
            list[i]=fileNode()
            list[i].path = currentNode.value.value.path
            list[i].name = currentNode.value.value.name
            delete_by_node(L,currentNode)
            i += 1
            if nextNode==None:
                break
        return print_array(list)
    else:
        print("no document found")


# busca en otra hash table (en una sub-carpeta)
def search_folder(hash_path, L,key_word):
    hash=load_structure(hash_path,"estructura")
    for i in range(0, len(hash)):

        if hash[i] != None:
            hashSlot = hash[i].value.head
            while hashSlot != None:
                nodoArchivo = hashSlot.value
                if nodoArchivo.isFolder:  # currentnode.value == type(lista):
                    search_folder(nodoArchivo.path, L)
                else:
                    relevance = occurrence(nodoArchivo.name, key_word)

                    if relevance > 0:
                        newNode = relevanceNode()
                        newNode.relevance = relevance
                        newNode.value = hashSlot.value
                        add(L, newNode)  # ,revelance
                hashSlot = hashSlot.nextNode

    return L


def search(key_word):
    main_path=os.getcwd()
    lista_archivos=os.listdir(main_path)
    existe=False
    for i in range(0,len(lista_archivos)):
        if lista_archivos[i]=="directorios_raiz":
            existe=True
            break
    if existe==True:
        lista_raiz = load_structure(main_path, "directorios_raiz")
        L = LinkedList()
        currentNode=lista_raiz.head
        while currentNode!=None:
            hash = load_structure(currentNode.value,"estructura")
            for i in range(0, len(hash)):

                if hash[i] != None:
                    hashSlot = hash[i].value.head
                    while hashSlot != None:
                        nodoArchivo=hashSlot.value
                        if nodoArchivo.isFolder:  # currentnode.value == type(lista):
                            search_folder(nodoArchivo.path, L,key_word)
                        else:
                            relevance = occurrence(nodoArchivo.name, key_word)

                            if relevance > 0:
                                newNode=relevanceNode()
                                newNode.relevance=relevance
                                newNode.value=hashSlot.value
                                add(L, newNode)  # ,revelance
                        hashSlot=hashSlot.nextNode
            currentNode=currentNode.nextNode
        order(L)
    else:
        print("No se ha creado ningun directorio previamente en el cual buscar.")