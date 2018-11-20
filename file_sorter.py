import os
import shutil


desktop_items = os.listdir("/home/stefan/Desktop")

picture = ["jpg" , "jpeg", "png"]
document = ["doc","docx","pdf","txt","pdf","odt","ppt","pptx","xls"]

for item in desktop_items:
	item_name =  str(item)
	for i in picture:
		if i in item_name:
			print(item_name)
			shutil.move("/home/stefan/Desktop/" + item,"/home/stefan/Desktop/Pics/" + item)
	for j in document:
		if j in item_name:
			print(item_name)
			shutil.move("/home/stefan/Desktop/" + item,"/home/stefan/Desktop/Docs/" + item)
