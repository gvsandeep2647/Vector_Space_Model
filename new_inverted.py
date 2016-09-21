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
	occurences = {}
	for word in l:
		d = {}
		for i in xrange(len(megaList)):
			temp = [j for j,val in enumerate(megaList[i][k]) if val==word]
			if temp :
				d[i+1] = temp
		occurences[word] = d
	return occurences	

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

ultraCategories = make_unique(ultraCategories)
dictCategories = {}
dictCategories = index1(ultraCategories,dictCategories,3)

ultraPost = make_unique(ultraPost)
dictPost = {}
dictPost = index1(ultraPost,dictPost,4)

