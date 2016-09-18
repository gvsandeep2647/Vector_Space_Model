from stemming import *
from nltk.tokenize import word_tokenize, RegexpTokenizer
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
    reader = csv.reader(readfile, skipinitialspace=False,delimiter=',', quoting=csv.QUOTE_NONE)
    writer = csv.writer(writefile,delimiter=' ',quotechar=' ',quoting=csv.QUOTE_MINIMAL)
    count = 0
    ite = 0 
    for row in reader:
        ite = ite + 1
        ultraList = []

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
            print count, ite


        blogger = row[2].split()
        ultraList.append(blogger)
        
        
        categories = row[3].split()    
        categories = row[3].split(':&:')
        categories = map(lambda x: x.strip(), categories)
        ultraList.append(normalizer(categories))
        
        post = row[4].split()
        ultraList.append(normalizer(post))

        #postlen

        outlinks = row[6]
        try:
            outlinks = int(outlinks)
        except Exception:
            print "Inconsistent Data Value of Outlinks"
        ultraList.append(outlinks)
        
        inlinks = row[7]
        try:
            inlinks = int(inlinks)
        except Exception:
            print "Inconsistent Data Value of Inlinks : "
        ultraList.append(inlinks)
        
        commentNo = row[8]
        commentNo = commentNo.strip()
        try:
            commentNo = int(commentNo)
        except:
            print "Inconsistent Data Value of CommentNo : "
        ultraList.append(commentNo)
        
        #commentURL
        
        permalink = row[10]
        ultraList.append(permalink)
        writer.writerow(ultraList)