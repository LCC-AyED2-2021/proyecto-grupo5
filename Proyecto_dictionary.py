from hash_structure.linkedlist import *
from hash_structure.algo1 import *
import math

class dictionary:
    key = None
    value=None

#funcion hash
def H(key,size):
    nkey=key % size
    return nkey

# h(k)=⌊m(k*A -⌊k*A⌋)⌋
def funcionHash(name, size):
    k = ord(name[0])
    ## valor de A recomendado Donald Knuth
    A = (math.sqrt(5) - 1) / 2
    key = math.floor(size * ((k * A) - math.floor(k * A)))
    return key

#accede al priemer elemento de la lista en la posicion key
def access(D,key):
    size=len(D)
    key=H(key,size)
    if D[key]!=None:
        return D[key].value.head
    else:
        return None

#inserta un key en una posicion determinada por la funcion de hash H(K)=K mod m
def insert(D,key,value):
    long=len(D)
    index=funcionHash(key, long)
    if D[index]==None:
        D[index]=dictionary()
        D[index].key=index
        D[index].value=LinkedList()
    add(D[index].value,value)
    return D

#Busca una key, si la encuentra devuelve su value sino devuevle None
def search(D,key):
    long = len(D)
    index = funcionHash(key, long)
    if D[index]!=None:
        currentChainNode=D[index].value.head
        while currentChainNode!=None:
            if currentChainNode.key==key:
                return currentChainNode.key
            currentChainNode=currentChainNode.nextNode
        return None
    else:
        return None

#elimina un nodo de la lista
def deleteChain(L,key):
    if L.head.key == key:
        L.head = L.head.nextNode
        return key
    else:
        currentChainNode = L.head
        while currentChainNode.nextNode != None:
            if currentChainNode.nextNode.key == key:
                currentChainNode.nextNode=currentChainNode.nextNode.nextNode
                return key
            currentChainNode = currentChainNode.nextNode
        return None

#elimina un key de la diccionario con hash
def delete(D,key):
    length=len(D)
    index=H(key,length)
    if D[index]!=None:
        return deleteChain(D[index].value,key)
    else:
        return None

#funcion hash por elemeneto(no utilizar metodo de la division porque es inficiente)
def hash_by_element(element,size):
    k=ord(element)
    A=(math.sqrt(5)-1)/2
    #A=math.pi
    variable=k*A
    parte_entera=math.floor(variable)
    key=math.floor((variable-parte_entera)*size)
    return key

#insert con hash por elemento
def insert_by_element(D,element,key,final):
    lenght = len(D)
    index=hash_by_element(element,lenght)
    if D[index]==None:
        D[index]=dictionary()
        D[index].value=index
        D[index].value=LinkedList()
    if final:
        lastInsert(D[index].value, element, key)  #O(n)
    else:
        add_key(D[index].value, element, key) #O(1)
    return D

#search con hash por elemento
def search_by_element(D,element):
    lenght = len(D)
    index=hash_by_element(element,lenght)
    if D[index]!=None:
        currentChainNode=D[index].value.head
        while currentChainNode!=None:
            if currentChainNode.value==element:
                return currentChainNode.key
            currentChainNode=currentChainNode.nextNode
        return None
    else:
        return None

#elimina un nodo de la lista busca por elemento
def deleteChain_by_element(L,element):
    if L.head.value == element:
        L.head = L.head.nextNode
        return True
    else:
        currentChainNode = L.head
        while currentChainNode.nextNode != None:
            if currentChainNode.nextNode.value == element:
                currentChainNode.nextNode=currentChainNode.nextNode.nextNode
                return True
            currentChainNode = currentChainNode.nextNode
        return None

#delete con hash por elemento
def delete_by_element(D,element):
    lenght=len(D)
    index = hash_by_element(element, lenght)
    if D[index]!=None:
        if  deleteChain_by_element(D[index].value,element)==True:
            return index
        else:
            return None
    else:
        return Node

#intento de print de un diccionario
def printDictionary(A):
    long=len(A)
    for i in range(0,long):
        if A[i]!=None:
            currentVertex = access(A, i)
            currentAdjacent=currentVertex.nextNode
            print(currentVertex.value.value,end=": ")
            if currentAdjacent!=None:
                while currentAdjacent!=None:
                    print(currentAdjacent.value.value,end="")
                    if currentAdjacent.nextNode!=None:
                        print(", ",end="")
                    else:
                        print()
                    currentAdjacent=currentAdjacent.nextNode
            else:
                print()
        else:
            print()