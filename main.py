from stemming import *
from nltk.tokenize import word_tokenize
import csv 
import nltk
PS = PorterStemmer()

def normalizer(l):
	for i in range(0,len(l)):
		l[i] = PS.stem(l[i],0,len(l[i])-1)

	return l

with open('posts.csv','rb',) as readfile,open('postprocessing.csv','wb')as writefile:
    reader = csv.reader(readfile,delimiter=',',quotechar=' ')
    writer = csv.writer(writefile,delimiter=' ',quotechar=' ',quoting=csv.QUOTE_MINIMAL)

    for row in reader:
        #print row
        ultraList = []
        title = word_tokenize(row[0])
        ultraList.append(normalizer(title))
        date = row[1].split()
        ultraList.append(date)
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
        print ultraList

