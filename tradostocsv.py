from lxml import etree
import re
from os import listdir, chdir, remove
from os.path import isfile, join
# import subprocess

def get_file_in_folder(my_path):
	onlyfiles = [f for f in listdir(my_path) if isfile(join(my_path, f))]
	return onlyfiles

def initfile(file):
	tag_list = ['tmx','header','prop','body','tu','tuv','seg']
	tag_list2 = []
	tree = etree.parse(file)
	for elem in tree.iter():
		if elem.tag not in tag_list and elem.tag not in tag_list2:
			tag_list2.append(elem.tag)
	for element in tag_list2:
		for user in tree.xpath("/tmx/body/tu/tuv/seg/"+element):
			user.text = ""
	tree.write("out.xml",encoding="utf-8")
	return ("out.xml",tag_list2)	

def read_file(file,encode):
	with open(file,encoding=encode) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	return content

def parse_file(tag_list2,contenu):
	list_sortie = []
	list_lang = []
	for line in contenu:
		match = re.search(r".*xml:lang=\"(.*)\">",line)
		if match is not None:
			if match.group(1) not in list_lang:
				list_lang.append(match.group(1))
		for element in tag_list2:
			pattern1 = "<"+element+">"
			pattern2 = "</"+element+">"
			pattern3 = "<"+element+" x=\"[0-9]+\" type=\"[0-9a-zA-Z]+\">"
			pattern4 = "<"+element+" i=\"[0-9]+\" type=\"[0-9]+\" x=\"[0-9]+\">"
			pattern5 = "<"+element+" i=\"[0-9]+\">"
			pattern6 = "<"+element+" type=\"[0-9]+\">"
			pattern7 = "<"+element+" i=\"[0-9]+\" type=\"[0-9]+\">"
			pattern8 = "<"+element+" i=\"[0-9]+\" type=\"[a-zA-Z]+\">"
			pattern9 = "<"+element+" type=\"[a-zA-Z]+\">"
			pattern10 = "<"+element+" pos=\"[a-zA-Z]+\" x=\"[0-9]+\">"
			pattern11 = "<"+element+" i=\"[0-9]+\" x=\"[0-9]+\" type=\"[a-zA-Z]+\">"
			pattern12 = "<"+element+" pos=\"[a-zA-Z]+\" x=\"[0-9]+\" type=\"[a-zA-Z]+\">"
			pattern13 = "<"+element+" pos=\"[a-zA-Z]+\">"
			pattern14 = "<"+element+" pos=\"[a-zA-Z]+\" type=\"[a-zA-Z]+\">"
			line = re.sub(pattern1,"",line)
			line = re.sub(pattern2,"",line)
			line = re.sub(pattern3,"",line)
			line = re.sub(pattern4,"",line)
			line = re.sub(pattern5,"",line)
			line = re.sub(pattern6,"",line)
			line = re.sub(pattern7,"",line)
			line = re.sub(pattern8,"",line)
			line = re.sub(pattern9,"",line)
			line = re.sub(pattern10,"",line)
			line = re.sub(pattern11,"",line)
			line = re.sub(pattern12,"",line)
			line = re.sub(pattern13,"",line)
			line = re.sub(pattern14,"",line)
		line = re.sub(r"&lt;b&gt;","",line)
		line = re.sub(r"&lt;/b&gt;","",line)
		line = re.sub(r"&lt;field name=\".*\"/&gt;","",line)
		line = re.sub(r"&lt;field name=\"Lettrine_Tx\"/&gt;","",line)
		line = re.sub(r"&lt;:cnmk 2&gt;","",line)
		line = re.sub(r"&lt;Lettr","",line)
		line = re.sub(r"&lt;Tab/&gt;","",line)
		line = re.sub(r"&lt;NewLine/&gt;"," ",line)
		line = re.sub(r"\(option.*\)","",line,flags=re.IGNORECASE)
		line = re.sub(r"&lt;:cnmk 7&gt;","",line)
		line = re.sub(r"&lt;BmkPoint id=.*/&gt;","",line)
		line = re.sub(r"&lt;:iaf [0-9]+&gt;","",line)
		line = re.sub(r"&lt;:hr&gt;","",line)
		line = re.sub(r"\(.*&gt;\)","",line)
		line = re.sub(r"&lt;:/cs&gt;","",line)
		line = re.sub(r"&lt;:cs \"[a-zA-Z]+\" [0-9]&gt;","",line)
		line = re.sub(r"&lt;:hs&gt;","",line)
		line = re.sub(r"&lt;Cond id=\"[0-9]+\" cond1=\"[a-zA-Z]+\"/&gt;","",line)
		line = re.sub(r"&lt;:/cns&gt;","",line)
		line = re.sub(r"&lt;:cns.*1&gt;","",line)
		line = re.sub(r"&lt;:cns.*2&gt;","",line)
		line = re.sub(r"&lt;i&gt;","",line)
		line = re.sub(r"&lt;/i&gt;","",line)
		line = re.sub(r"","",line)
		line = re.sub(r"","",line)
		line = re.sub(r"&lt;Cond id=\"[0-9]+\" cond1=\".*\"/&gt;","",line)
		line = re.sub(r"&lt;CondEnd id=\"[0-9]+\"/&gt;","",line)
		line = re.sub(r"&lt;/F&gt;","",line)
		line = re.sub(r"&lt;F id=\"[0-9]+\"&gt;","",line)
		line = re.sub(r"&lt;Frm id=\"[0-9]+\"/&gt;","",line)
		line = re.sub(r"&lt;Tbl id=\"[0-9]+\"/&gt;","",line)
		line = re.sub(r"&lt;u options=\".*\"&gt;","",line)
		line = re.sub(r"&lt;/u&gt;","",line)
		line = re.sub(r"&lt;:cnmk 6&gt;","",line)
		line = re.sub(r"&lt;mark id=\"[0-9]+\" type=\".*\"/&gt;","",line)
		line = re.sub(r"&lt;Char value=\"[0-9]+\" fontid=\"[0-9]+\"/&gt;","",line)
		line = re.sub(r"&lt;:fc [0-9]+&gt;","",line)
		line = re.sub(r"&lt;:/fc&gt;","",line)
		line = re.sub(r"&lt;:gt&gt;","",line)
		line = re.sub(r"&amp;","",line)
		line = re.sub(r"&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;&lt;p id=\"[0-9]+\"&gt;&lt;/p&gt;&lt;/frame&gt;&lt;/chapter&gt;&lt;/body&gt;&lt;/doc&gt;&lt;/tff&gt;","",line)
		line = re.sub(r"&gt;","",line)
		line = re.sub(r"&lt;","",line)
		match = re.search(r"<seg>(.*)</seg>",line)
		if match is not None:
			# print(match.group(1))
			list_sortie.append(match.group(1))
	return (list_sortie,list_lang)

def prepare_output(list_lang,list_sortie):
	i = 1
	to_file = []
	str1 = ';'.join(list_lang)
	to_file.append(str1)
	for ligne in list_sortie:
		if i == 1:
			ligne_tableau = ligne + ";"
			i = i + 1
		else:
			ligne_tableau = ligne_tableau + ligne
			i = 1
			to_file.append(ligne_tableau)
			ligne_tableau = ""
	return to_file

def write_in_file(fichier,to_file):
	filename_output = ""
	match = re.search(r"(.*)\.(tmx|TMX)",fichier)
	if match is not None:
		filename_output = match.group(1)+".csv"
	file = open(filename_output,"w")
	for line in to_file:
		file.write(line)
		file.write("\n")
	file.close()
	return "DONE"





my_path = ""
file_folder = get_file_in_folder(my_path)
chdir(my_path)
for fichier in file_folder:
	if fichier != "out.xml" and not fichier.endswith("csv"):
		print("Traitement de "+fichier+" : EN COURS")
		(fichier2,tag_list2) = initfile(fichier)
		contenu = read_file(fichier2,"utf-8")
		(list_sortie,list_lang) = parse_file(tag_list2,contenu)
		to_file = prepare_output(list_lang,list_sortie)
		traitement = write_in_file(fichier,to_file)
		print("Traitement de "+fichier+" : "+traitement)

remove("out.xml")


