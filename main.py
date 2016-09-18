from stemming import *
from nltk.tokenize import word_tokenize
import csv 
import nltk
import time
import re
PS = PorterStemmer()

def normalizer(l):
	for i in range(0,len(l)):
		l[i] = PS.stem(l[i],0,len(l[i])-1)

	return l

def _callback(matches):
	id = matches.group(1)
	try:
		return unichr(int(id))
	except:
		return id

def decode_unicode_references(data):
	return re.sub("and#(\d+)(;|(?=\s))|&#(\d+)(;|(?=\s))", _callback, data)


with open('posts.csv','rb',) as readfile,open('postprocessing.csv','wb')as writefile:
    reader = csv.reader(readfile,delimiter=',',quotechar=' ')
    writer = csv.writer(writefile,delimiter=' ',quotechar=' ',quoting=csv.QUOTE_MINIMAL)

    for row in reader:
        ultraList = []
        

        title = re.sub('[^a-zA-Z0-9 ]','',decode_unicode_references(row[0]))
        title = word_tokenize(str(title))

        ultraList.append(normalizer(title))
        
        date = row[1].split()
        try :
            date[3] = date[3][:-2]
            string = date[0]+" "+date[1]+" "+date[2]+" "+date[3]
            struct_time = time.strptime(string, "%b %d %Y %H:%M")  
            secs = time.mktime(struct_time)
            ultraList.append(secs)
        except Exception:
            ultraList.append(date)

        blogger = re.sub('[^a-zA-Z0-9 ]','',decode_unicode_references(row[2]))
        blogger = word_tokenize(str(blogger))
        ultraList.append(blogger)
        
        categories = row[3].split()
        ultraList.append(normalizer(categories))
        
        post = re.sub('[^a-zA-Z0-9 ]','',decode_unicode_references(row[4]))
        post = (word_tokenize(str(post)))
        ultraList.append(normalizer(post))
        #postlen
        outlinks = row[6].split()
        ultraList.append(outlinks)
        
        inlinks = row[7].split()
        ultraList.append(inlinks)
        
        commentNo = row[8].split()
        ultraList.append(commentNo)
        #commentURL
        permalink = row[10].split()
        ultraList.append(permalink)
        writer.writerow(ultraList)

