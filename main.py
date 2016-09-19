from stemming import *
from nltk.tokenize import RegexpTokenizer
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

megaList = [] 
with open('posts.csv','rb',) as readfile,open('postprocessing.csv','wb')as writefile:
    reader = csv.reader(readfile, skipinitialspace=False,delimiter=',', quoting=csv.QUOTE_NONE)
    count = 0
    ite = 0
    tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+') 
    for row in reader:
        ite = ite + 1
        ultraList = []
                
        title = re.sub('[^\x00-\x7F]','',decode_unicode_references(row[0]))
        title = tokenizer.tokenize(str(title))
        title = [x.strip(' ') for x in title]
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


        blogger = re.sub('[^\x00-\x7F]','',decode_unicode_references(row[2]))
        blogger = tokenizer.tokenize(str(blogger))
        blogger = [x.strip(' ') for x in blogger]
        ultraList.append(blogger)

        if not row[3]:
            categories = row[3].split()
            categories = [x.strip(' ') for x in categories]
        else:
            categories = row[3].split(':&:')
            categories = [x.strip(' ') for x in categories]
        ultraList.append(normalizer(categories))

        post = re.sub('[^\x00-\x7F]','',decode_unicode_references(row[4]))
        post = tokenizer.tokenize(str(post))
        post = [x.strip(' ') for x in post]
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


        megaList.append(ultraList)



