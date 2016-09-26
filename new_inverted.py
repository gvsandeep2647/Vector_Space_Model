"""
  
  ASSIGNMENT #1
  Project : To build an IR model based on a vector space model 
  
  Instructor : Dr. Aruna Malapati
  
  Contributors : G V Sandeep 2014A7PS106H
                 Kushagra Agrawal 2014AAPS334H
                 Snehal Wadhwani 2014A7PS430H

  Course No : CS F469 Information Retrieval

  Working of new_inverted.py:
    1. This python script creates an inverted index for title,posts and blogger
    2. This done by first aggregating all the words in title,posts and blogger and making them unique (Eleminating the repeated values).
	3. The inbuilt facility of making a list a set and vice versa has been used to achive this task.

"""
from main import *
from collections import *


ultraTitle = []
ultraBlogger = []
ultraCategories = []
ultraPost = []

def make_unique(l):
	'''
		Making the list a set to eliminate all the duplicates and then converting it back to list
	'''
	l = set(l)
	l = list(l)
	return l

def index1(l,d,k):
	'''
		Creates an inverted index.
		It basically returns a dictionary with each key as a word
		Each key then has a value as a dictionary with doc id as key and a list of positional occurences as value
	'''
	occurences = {}
	for word in l:
		d = {}
		for i in xrange(len(megaList)):
			temp = [j for j,val in enumerate(megaList[i][k]) if val==word]
			if temp :
				d[i] = temp
		occurences[word] = d
	
	return occurences
'''
	Aggregating all the words from titles,posts and bloggers into indivdual lists
'''
for row in megaList:
	for j in row[0]:
		ultraTitle.append(j)
	for j in row[2]:
		ultraBlogger.append(j)
	for j in row[3]:
		ultraCategories.append(j)
	for j in row[4]:
		ultraPost.append(j)

ultraTitle = make_unique(ultraTitle)
dictTitle = {}
dictTitle = index1(ultraTitle,dictTitle,0)

ultraBlogger = make_unique(ultraBlogger)
dictBlogger = {}
dictBlogger = index1(ultraBlogger,dictBlogger,2)

ultraPost = make_unique(ultraPost)
dictPost = {}
dictPost = index1(ultraPost,dictPost,4)

ultraCategories = make_unique(ultraCategories)
