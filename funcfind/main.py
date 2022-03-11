import os
import sys


# python main,py dir_name phrase
## return list of files of phrase found


head_list = []

def searchfile(phrase,file):
	try:
		file = open(file,"r")
		data = file.read()
		result = data.find(phrase)
		if result == -1:
			return False
		return True
	except:
		print("Error reading file.")


def search_dir(dir,phrase):
	data = os.listdir(dir)
	file = []
	folder = []
	rest = []
	for element in data:
		if os.path.isdir(dir +"/" + element):
			folder.append(dir +"/" + element)

		if os.path.isfile(dir +"/" + element):
			file.append(dir +"/" + element)


	for f in file:
		if searchfile(phrase,f):
			head_list.append(f)
	
	if len(folder) == 0:
		return head_list

	for d in folder:
		search_dir(d,phrase)

	

dir_name = sys.argv[2]
phrase = sys.argv[1]


search_dir(dir_name,phrase)

for element in head_list:
	print(element)