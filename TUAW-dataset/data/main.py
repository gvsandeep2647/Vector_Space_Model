"""
  
  ASSIGNMENT #1
  Project : To build an IR model based on a vector space model 
  
  Instructor : Dr. Aruna Malapati
  
  Contributors : G V Sandeep 2014A7PS106H
                 Kushagra Agrawal 2014AAPS334H
                 Snehal Wadhwani 2014A7PS430H

  Course No : CS F469 Information Retrieval

  Working of main.py:
    1. The entire corpus is read and each row is stored as a list.
    2. Each list is broken down to it's attributes and appropriate tokenization and normalization is apllied.
    3. The title,blogger's name and post is stripped of some special characters and then is stemmed using Porter's Stemming Algorithm
    4. Date is converted to a floating point timestamp
    5. Postlength and Comment URL have been ignored in the final processed dataset as they add no value to the corpus
    6. No of inlinks, outlinks and comments have been normalized using the formula (1+log(num)) where num is their value. This is because twice the number of comments do not increase the relevance of my document by twice.

    This list is then send to the new_inverted.py file which generates indexes.

"""
from stemming import * 
'''
    Package for implementing stemming 
'''
from nltk.tokenize import RegexpTokenizer
''' 
    Used for tokenizing the given dataset on the basis of required special characters
'''
import csv
'''
    A package used for reading the csv files into the python programs
''' 
import math
import time
import re
'''
    Facilitates implementing regular expression based splitting 
'''
PS = PorterStemmer()

TITLE = 0.25
BLOGGER = 0.2
POST = 0.16
INLINKS = 0.09
OUTLINKS = 0.2
COMMENTS = 0.1

""" 
    Normalizer :Parameter : A list
                Returns : A list

    Takes each word in the given list and stems it according to the Porter's Stemming Algorithm  
"""
def normalizer(l):
    for i in range(0,len(l)):
        l[i] = PS.stem(l[i],0,len(l[i])-1)

    return l
"""

    _callback and decode_unicode_references will convert all the HTML Entities into characters defined by the ASCII character set.
    This is done using inbuilt functions of the re package

"""

def _callback(matches):
    id = matches.group(1)
    try:
        return unichr(int(id))
    except:
        return id

def decode_unicode_references(data):
    return re.sub("and#(\d+)(;|(?=\s))|&#(\d+)(;|(?=\s))", _callback, data)

def escape(data):
    """HTML-escape the text in `t`."""
    return (data
        .replace("andamp", "&").replace("andlt", "<").replace("andgt", ">")
        .replace("and#39", "'").replace('andquot', '"')
        )

megaList = []   # Will hold the corpus  
with open('testing.csv','rb',) as readfile:
    reader = csv.reader(readfile, skipinitialspace=False,delimiter=',', quoting=csv.QUOTE_NONE)
    tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+') #holds the regular expression which would be used to tokenize words 
    for row in reader:
        ultraList = [] #One Row of the CSV File
        
        #title will finally hold the normalized list of words of the row's title.
        raw_title = row[0]
        title = re.sub('[^\x00-\x7F]','',escape(decode_unicode_references(row[0])))
        title = tokenizer.tokenize(str(title))
        title = [x.strip('-.?/') for x in title]  
        title = filter(None,title)
        title = normalizer(title)
        ultraList.append(title)
        
        
        #date will finally hold a UNIX friendly timestamp
        date = row[1].split()
        try :
            date[3] = date[3][:-2]
            string = date[0]+" "+date[1]+" "+date[2]+" "+date[3]
            struct_time = time.strptime(string, "%b %d %Y %H:%M")  
            secs = time.mktime(struct_time)
            ultraList.append(secs)
        except Exception:
            ultraList.append(date)

        #blogger will finally hold the normalized list of words of the row's blogger.
        blogger = re.sub('[^\x00-\x7F]','',escape(decode_unicode_references(row[2])))
        blogger = tokenizer.tokenize(str(blogger))
        blogger = [x.strip('-.?/') for x in blogger]
        blogger = filter(None,blogger)
        ultraList.append(blogger)

        #categories will finally hold the normalized list of words of the row's categories.
        categories = re.sub('[^\x00-\x7F]','',escape(decode_unicode_references(row[3])))
        if not row[3]:
            categories = row[3].split()    
        else:
            categories = row[3].split(':&:')
        categories = [x.strip(' ') for x in categories]
        catergoies = filter(None,categories)
        ultraList.append(normalizer(categories))

        #posts will finally hold the normalized list of words of the row's posts.
        post = re.sub('[^\x00-\x7F]','',escape(decode_unicode_references(row[4])))
        post = tokenizer.tokenize(str(post))
        post = [x.strip('-.?/;') for x in post]
        post = filter(None,post)
        ultraList.append(normalizer(post))

        #postlen has been ignored as it doesn't add value to the corpus
        
        #outlinks will finally contain the normalized number of outlinks.It's normalized using the formula 1+log10(num) where num is its value
        outlinks = row[6]
        try:
            outlinks = int(outlinks)
        except Exception:
            print "Inconsistent Data Value of Outlinks"
        if outlinks == 0:
            pass
        else:    
            outlinks = 1 + math.log10(outlinks)
        ultraList.append(outlinks)
        
        #inlinks will finally contain the normalized number of inlinks.It's normalized using the formula 1+log10(num) where num is its value
        inlinks = row[7]
        try:
            inlinks = int(inlinks)
        except Exception:
            print "Inconsistent Data Value of Inlinks : "
        if inlinks == 0:
            pass
        else:
            inlinks = 1 + math.log10(inlinks)
        ultraList.append(inlinks)
        
        #commentNo will finally contain the normalized number of commentNo.It's normalized using the formula 1+log10(num) where num is its value
        commentNo = row[8]
        commentNo = commentNo.strip()
        try:
            commentNo = int(commentNo)
        except:
            print "Inconsistent Data Value of CommentNo : "
        if commentNo == 0:
            pass
        else :    
            commentNo = 1 + math.log10(commentNo)
        ultraList.append(commentNo)
        
        #commentURL has been ignore as it adds no value to the corpus
        
        #permalink contains the permalink of the document. 
        permalink = row[10]
        ultraList.append(permalink)
        ultraList.append(raw_title)
        megaList.append(ultraList)