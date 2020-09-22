import time
import requests
import random
import string
import concurrent.futures

def load_image_list():
	file = open('list.csv','r')
	lines = file.readlines()
	data = []
	for line in lines:
		line = line[:-1]
		data.append(line)
	return data

def download(img_url):
	img_bytes = requests.get(img_url).content
	letters = string.ascii_lowercase
	name = ''.join(random.choice(letters) for i in range(13))	
	img_name = name + '.jpg'
	print(img_name)
	with open('../Wallpapers/'+img_name,'wb') as img_file:
		img_file.write(img_bytes)
		print('done')


start = time.perf_counter()

img_urls = load_image_list()

with concurrent.futures.ThreadPoolExecutor() as executor:
	executor.map(download,img_urls)


end = time.perf_counter()

print(end-start)