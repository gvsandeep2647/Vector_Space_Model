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

with open('posts.csv','rb',) as readfile,open('postprocessing.csv','wb')as writefile:
    reader = csv.reader(readfile,delimiter=',',quotechar=' ')
    writer = csv.writer(writefile,delimiter=' ',quotechar=' ',quoting=csv.QUOTE_MINIMAL)
    count = 0
    for row in reader:
        ultraList = []

        row[0] = re.sub('\W+',' ', row[0] )
        title = word_tokenize(row[0])
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
            count = count + 1
            print count


        blogger = row[2].split()
        ultraList.append(blogger)
        
        categories = row[3].split()
        ultraList.append(normalizer(categories))
        
        post = row[4].split()
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

