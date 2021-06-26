import os
from personal_library import *

#create("D:\Documentos de Usuario\Desktop\Test-Dataset")
#search("covid")

exit = False
while not exit:
	print("Que desea hacer?")
	print("1. Create")
	print("2. Search")
	print("3. Exit")
	option = input("")
	print("")

	if option == "1":
		isFile = False
		while isFile == False:
			local_path = input("Enter the directory path: ")
			isFile = os.path.isdir(local_path)
			if isFile == False:
				print("error: no directory found.")
				print("")
		create(local_path)
		print("")
	elif option == "2":
		key_word = input("enter the keyword: ")
		print("")
		search(key_word)
		print("")
	else:
		exit = True
		print("Program Finished")

