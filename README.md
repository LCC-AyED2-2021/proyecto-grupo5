<<<<<<< develop
# P_grupo5
=======
# Proyecto Semestral, Algoritmos II (GRUPO 5: COGO, LANA, MONTAÑO)


## Título: Generación de biblioteca virtual para búsquedas de documentos relevantes.


### Objetivos Generales

Desarrollar una aplicación para manejar una biblioteca virtual de documentos utilizando una estructura de datos previamente definida en la misma aplicación.
Desarrollar mecanismos eficientes de consultas sobre los documentos de la biblioteca.
Requerimientos

Lograr el cumplimiento de los objetivos a través de una aplicación (script) utilizando el lenguaje de programación python3.
A través de la aplicación desarrollada, permitir la creación de la biblioteca utilizando una dirección local (un directorio del propio ordenador) que contiene los documentos que componen la biblioteca.
Para la creación de la biblioteca se utilizará el siguiente comando: python personal_library.py -create <local_path>
Una vez cargados los documentos en la aplicación (creación de la biblioteca), permitir realizar consultas sobre el contenido de los documentos en la biblioteca.
Para la generación de consultas se utilizará el siguiente comando: python personal_library.py -search <key_word>
Para el desarrollo de la aplicación solamente queda permitido el uso de algunas estructuras y tipos de datos nativos de python como: array, list, boolean, int y string y la biblioteca math. El resto de las estructuras utilizadas deben ser exclusivamente implementadas por el equipo de trabajo.
Garantizar la persistencia de los datos. Esto significa que todos los documentos de la biblioteca tienen que ser recuperables a través de consultas en todo momento.
Los equipos de trabajo deben estar compuestos por 2 estudiantes. No se permiten trabajos individuales y en caso de que el número total de estudiantes sea impar se conformará solamente un equipo de 3 estudiantes. 

### Evaluación del proyecto

. Para la evaluación del proyecto entra en consideración los siguientes factores: 
. Perfecto entendimiento de cada integrante del equipo de todo el código del proyecto.

. Perfecto entendimiento de cada integrante del equipo de los problemas surgidos y soluciones generadas durante toda la fase de desarrollo de la aplicación.

. Correcto funcionamiento de la aplicación acorde a los objetivos planteados. 

. Claridad y documentación del código.

. Correcta elección de las estructuras de datos y algoritmos utilizados.

. Eficiencia de la aplicación relacionada al costo temporal y espacial.

### Creación de la Biblioteca

Para la creación de la biblioteca se utilizará el siguiente comando: python personal_library.py -create <local_path>
<local_path> representa la dirección local de la carpeta que contiene los documentos de la biblioteca.
Una vez finalizado el proceso de creación de la biblioteca la aplicación devolverá el texto “library created successfully”. A partir de este momento se pueden iniciar las búsquedas.
La biblioteca deberá persistir la información de manera que se pueda acceder a sus documentos en todo momento. Esto significa que no se deberá volver a crear la biblioteca en cada búsqueda, sino que se realizará sobre una estructura persistente en disco, que se levantará a memoria cada vez que se requiera hacer una consulta.

### Búsquedas de documentos

La búsqueda de documentos se va a realizar a través de palabras claves. Para ellos se utilizará el comando: python personal_library.py -search <key_word>.
El resultado de una búsqueda a través de una palabra clave (<key_word>) va a devolver todos los títulos de los documentos que contienen esa palabra clave en su texto ordenados por relevancia. 
La relevancia se calcula por el número de ocurrencias de la palabra clave en el documento. Los documentos con mayor relevancia irán primero en el resultado de la búsqueda.
En caso de no existir ningún documento en la biblioteca que contenga la palabra clave se devolverá el texto: “no document found”.

### Estructura de la Aplicación a realizar

Se implementará un script en python utilizando la versión 3. El script tendrá el nombre personal_library.py. Sobre ese script se realizarán las operaciones de creación y búsqueda. El manejo de errores, excepciones y posibles valores de entrada corren a cargo de los desarrolladores de la aplicación. Dicho script será utilizado para realizar las pruebas para evaluar el desempeño de la aplicación.


### Modelo y Estructura del proyecto

![image](https://user-images.githubusercontent.com/53227496/122651019-81a7c280-d10c-11eb-83a1-d605a511f654.png)


El programa comienza recibiendo un local_path dado por el usuario acompañado de la funcion -create. Esto genera una LinkedList a la cual denominamos Shelf(estantería). Dentro de ésta existen un conjunto de nodos. Y dentro de cada nodo hay 2 atributos. El atributo nextNode, y el atributo value que contiene un nodo Diccionario. A su vez, este nodo Diccionario está formado por otros 2 atributos: key y value.
 
 -key: Contiene el nombre del archivo de texto.
 
 -value: Dentro de este, se encuentra un Hashtable llamado Book.
 
 En cada slot del book se encontrará una LinkedList. Cada uno de sus nodos, contendrá en su atributo value un nuevo nodo de tipo archivo(fileNode). 
 El nodo fileNode tiene los siguientes atributos:
 
 -word: Por defecto tipo None. En este se incluirá un String de la librería algo1.py. 
 
 -entry: Por defecto con valor 0. Este atributo funciona como contador de reiteraciones que realiza el String contenido en el atributo word dentro del archivo de texto.
 
 Una vez leidos e indexados todos los archivos de texto contenidos en el local_path, finaliza la función -create. En este punto ya podremos llevar a cabo la ejecución de la funcion -search. 

 
 
 ## Especificaciones y funcionamiento de la función -create:
 
 La función -create actúa de la siguiente manera: 
 1. Crea un Nodo en la lista y ubica un nodo de tipo Diccionary que tiene dentro el nombre del archivo y un Hashtable.
 2. La función comenzará a leer el archivo, recorrerá línea por línea y separará palabra por palabra.
 3. Tomará cada palabra, y utilizando una función Hash la introducirá en el Hashtable.(*)
 4. Cuando finalice el indexado de todas las palabras de un archivo, pasará al siguiente archivo de texto.
 5. Cuando no existan mas archivos por leer, finaliza la función.
 
 (*) En caso de que se dé la existencia de 2 palabras iguales, se producirá el aumento del contador entry del fileNode al cual corresponda esa palabra.
 
 
 ## Especificaciones y funcionamiento de la función -search:
 
 La función -search actúa de la siguiente manera: 
 1. Se ejecuta con un parámetro keyword ingresado por el usuario.
 2. Luego, ingresa a la LinkedList donde se encuentran listados los Hashtables asociados a un nombre de archivo. 
 3. Se ejecuta la función Hash para hallar la ubicación del Slot donde podría encontrarse la palabra buscada o keyword dentro de una LinkedList.
 4. Si se encuentra la keyword, se ingresará en una nueva LinkedList de relevancia el nombre del archivo donde se encuentra la keyword y el valor del atributo entry.
 5. Cada vez que se crea un nuevo nodo en la LinkedList de relevancia, el mismo se irá ordenando de mayor a menor dependiendo del valor del atributo entry.
 6. Ya habiendo terminado de revisar toda la LinkedList Shelf, se imprime la LinkedList de relevancia. 
 

## Complejidad de las funciones
L = cantidad de caracteres linea con mas caracteres 
S = cantidad de slots del hash mas grande

### Función Create(): 

<<<<<<< HEAD

### Función Search():


### Función ReHashing():

=======
#O(L^4*S)

### Función Search():

#O(S^2*L^2)

### Función ReHashing():

#O(S^2)

>>>>>>> 576dd444a927fd884d51647b284daa113ff70d93
>>>>>>> main
