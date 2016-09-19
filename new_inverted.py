from main import megaList
ultraTitle = []
ultraBlogger = []
ultraCategories = []
ultraPost = []

def make_unique(l):
	l = set(l)
	l = list(l)
	return l

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
ultraBlogger = make_unique(ultraBlogger)
ultraCategories = make_unique(ultraCategories)
ultraPost = make_unique(ultraPost)

print ultraBlogger