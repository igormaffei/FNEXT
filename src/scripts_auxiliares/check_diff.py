import os

img_files = os.listdir("datasets/imgs")
cap_files = os.listdir("datasets/captions")

checklist = []

for file in cap_files:
	file_name = file.split('.')
	checklist.append(file_name[0])

for file in img_files:
	file_name = file.split('.')
	if file_name[0] not in checklist:
		print("Not found: ",file)
	