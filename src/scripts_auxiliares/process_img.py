
import csv
import json
from datetime import date, datetime
import urllib.request
import os

idSup = [2252, 2245, 2231, 2223, 2162, 2161, 2143, 2064, 2039, 1964, 1921, 1911, 1873, 1801, 1678,
		 1818, 1817, 1741, 1667, 1661, 1542, 1540, 1521, 1497, 1496, 1407, 1399, 1386, 1385, 1279,
		 1276, 1274, 1272, 1265, 1245, 1233, 1230, 1132, 1128, 1046, 1043,    7,    3,    1]

idApagar = [2111, 2023, 1935, 1911, 1896, 1889, 1883, 1826, 1791, 1776, 1727, 1725, 1793, 1673, 1573,
			1557, 1519, 1501, 1495, 1423, 1356, 1300, 1278, 1264, 1263, 1260, 1258, 1257, 1256, 1255,
			1254, 1251, 1231, 1228, 1227, 1199, 1178, 1110, 1104, 1080, 1079, 1071, 1068,  983,  955,
			 920,  892,  885,  856,  855,  831,  827,  821,  819,  744,  737,  669,  659,  588,  576,
			 301,  300,  299,  296,  295,  293,  287,  285,  282,  278,  277,  272,  271,  268,  265,
			 262,  261,  258,  255,  254,  250,  242,  239,  228,  221,  220,  219,  213,  202,  200,
			 199,  198,  196,  194,  190,  189,  188,  185,  184,  182,  181,  180,  178,  177,  176,
			 176,  174,  171,  162,  159,  158,  157,  155,  138,  133,  131,  130,  129,  127,  120,
			 116,  113,  107,  106,  103,   99,   97,   94,   90,   87,   86,   85,   83,   80,   77,
			  74,   71,   64,   63,   60,   49,   44,   42,   38,   37,   36,   32,   29,   27,   26,
			  18,   15,   14]

def get_img_path(row):
	id = row[0]
	folder = "fake" if row[6] == "FALSO" else "notFake"
	file_path = "News/{}/{}/news content.json".format(folder, id)
	
	img = None
	with open(file_path) as json_file:
		data = json.loads(json_file.read())
		img = data['top_img']

	print(img)
	
	return img   	

def save_img(url, id):
	#img_data = requests.get(url).content

	#with open("imgs/{}.jpeg".format(id), 'wb') as handler:
	#	handler.write(img_data)
	try:

		r = urllib.request.urlopen(url)
		with open("imgs/{}.jpeg".format(id), "wb") as f:
			f.write(r.read())

		return True
	except: 
		return False

def process_csv(file_path_origin, file_path_dest):
	with open(file_path_origin, 'r') as f_in, open(file_path_dest, 'w') as f_out:
		csv_reader = csv.reader(f_in, delimiter=';')
		writer = csv.writer(f_out)

		isFirst = True
		for row in csv_reader:
			if not isFirst:
				img = get_img_path(row)
				
				if save_img(img, row[0]):
					row.append(img)
				
				writer.writerow(row)

			isFirst = False

def delete_img():
	count = 0
	for id in idApagar:
		print("{}.jpeg".format(id))
		if os.path.exists("imgs/{}.jpeg".format(id)):
			os.remove("imgs/{}.jpeg".format(id))
		count = count + 1
	
	print("total: {}".format(count))

def clean_csv_img_column(file_path_origin, file_path_dest):
	with open(file_path_origin, 'r') as f_in, open(file_path_dest, 'w') as f_out:
		csv_reader = csv.reader(f_in, delimiter=',')
		writer = csv.writer(f_out)

		isFirst = True
		count = 0

		for row in csv_reader:
			if not isFirst:
				if not os.path.exists("imgs/{}.jpeg".format(row[0])):
					print("{} - NÃO TEM".format(row[0]))
					if len(row) >= 8: row[7] = None
				else:
					count = count + 1
					print("{} - TEM".format(row[0]))


			writer.writerow(row)		
			isFirst = False

		print("total: {}".format(count))


if __name__ == "__main__":
	print("<INICIO>") 
	#process_dataset("fakenewssetbase-utf8.csv")
	#process_csv("fakenewssetbase-utf8.csv","fakenewssetbase-img.csv")
	#delete_img()
	#clean_csv_img_column("fakenewssetbase-img.csv","fakenewssetbase-img-adjust.csv")
	print("<FIM>")



	          