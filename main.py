from personal_library import *
import pickle
from hash_structure.algo1 import *

"python personal_library.py -create <local_path>"
"python personal_library.py -search <key_word>"
option=None
#D:\Documentos de Usuario\Desktop\carpeta pruebas
while option != "3" and option != "salir":
    print("1.Crear archivo/carpeta")
    print("2.Buscar archivo")
    print("3.Salir")
    option = input("")

    if option == "1":
        ## verifica si existe la direccion
        existe = False
        while existe == False:
            local_path = input("Ingrese la direccion donde creará su archivo: ")
            existe = os.path.isdir(local_path)
            if existe == False:
                print("La direccion no es una carpeta, introduzcala nuevamente")
        create(local_path)
    elif option == "2":
        searchedWord = input("Ingrese una palabra clave para encontrar su archivo: ")
        search(searchedWord)
    else:
        exit = True