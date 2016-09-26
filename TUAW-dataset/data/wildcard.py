'''import re
regex = re.compile('th.s')
l = ['this', 'is', 'just', 'a', 'test']
matches = [string for string in l if re.match(regex, string)]
print matches	
'''
from Tkinter import *
import ttk
import datetime
import time
from new_inverted import ultraCategories,dictTitle
from main import *	
from stemming import *
from nltk.tokenize import RegexpTokenizer
from tfidf import *
from math import log

def rotate(str, n):
	return str[n:] + str[:n]

#print dictTitle
file = open("Permutermindex.txt","w")
keys = dictTitle.keys()
for key in sorted(keys):
	dkey = key + "$"
	for i in range(len(dkey),0,-1):
		out = rotate(dkey,i)
        file.write(out)
        file.write(" ")
        file.write(key)
        file.write("\n")
file.close()
