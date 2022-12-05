import os

img_files = os.listdir("datasets/imgs")
for file in img_files:
	file_name = file.split('.')
	print(file, file_name[0])
	os.system("curl -F \"image=@datasets/imgs/{}\" -X POST http://localhost:5000/model/predict > datasets/captions/{}.json"
		.format(file, file_name[0]))
