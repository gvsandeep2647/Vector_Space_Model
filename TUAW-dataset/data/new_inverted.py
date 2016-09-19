from main import megaList
from collections import defaultdict
ultraTitle = []
ultraBlogger = []
ultraCategories = []
ultraPost = []

def make_unique(l):
	l = set(l)
	l = list(l)
	return l

def index1(l,d,k):
	temp = []
	for i in l:
		for j in range(0,len(megaList)):
			if i in megaList[j][k]:
				temp1    = [0,0,0]
				temp1[0] = i
				temp1[1] = megaList[j][k].count(i)
				temp1[2] = j
				temp.append(temp1)

	for i in temp:
		if i[0] in d:
			pass
			#d[i[0]] = d[i[0]].append([i[1],i[2]])
		else:
			d[i[0]] = [i[1],i[2]]
	print d['isight']

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
# for i in ultraTitle:
# 	for j in range(0,len(megaList)):
# 		if i in megaList[j][0]:
# 			dictTitle[i] = j

#for d in dictTitle:
#	print d, dictTitle[d]
ultraBlogger = make_unique(ultraBlogger)
ultraCategories = make_unique(ultraCategories)
ultraPost = make_unique(ultraPost)

