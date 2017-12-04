# -*- coding: utf-8 -*-
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")
import csv
import unicodedata
from pattern.vector import NB, kfoldcv, count,KNN,Document,Model

#Funcion para remover acentos
def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', unicode(input_str))
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

#para crear nuevo archivo sin acentos
sinAcentos = open('sin_acentos.txt', 'w')
#abre el archivo que se le quitaran acentos (training)
with open('training amor.txt') as f:
    read = csv.reader(f)
    for row in read:
        for element in row:
            sinAcentos.write(remove_accents(element))
#cierra el archivo
sinAcentos.close()
#abre archivo sin acentos
f = open('sin_acentos.txt', 'r')
#separa por tweets
for line in f.readlines():
	line = line.strip()
	tweets = line.split("tweet:")
	

#abre diccionario de palabras de personas comunes
with open('opiniones.txt') as g: 
	comunes = [line.strip('\n') for line in g]

#busca las palabras del diccionario en los tweets
result = open('result.txt','w')
for str in tweets:
	for palabrita in comunes:
		if set(palabrita.split()) & set(str.split()):
			
			# escribe opinion/tweet
			result.write("opinion"+"/"+ str + "\n")
		else:
			result.write("noticia"+"/"+ str + "\n")

result.close()

result=open('result.txt',"r")


documents=[]

for linea in result.readlines():
	document = Document(linea.split("/")[1], type=linea.split("/")[0])
	documents.append(document)

m = Model(documents)


nb=NB()

for document in m:
    nb.train(document)

print nb.classify("opinion")
print nb.classify("noticia")

from pattern.vector import k_fold_cv
print k_fold_cv(NB, documents=m, folds=10)

	
#for palabra in lines:
#	print d.get(palabra)
"""
1. Sacar bien los resultados 
	#HuracanPatricia
	#AguaEnMarte
2. Modificar poster de acuerdo a los resultados y enfocarse en el desarrollo 
"""
