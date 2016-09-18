import csv
with open('sandeep.csv','rb',) as readfile,open('postprocessing.csv','wb')as writefile:
    reader = csv.reader(readfile,delimiter=',',quotechar=' ')
    writer = csv.writer(writefile,delimiter=' ',quotechar=' ',quoting=csv.QUOTE_MINIMAL)
    ite = 0
    for row in reader:
    	ite = ite + 1
    	if ite == 1843:
			print row[0]
			print row[1]
			print row[2]
			print row[3]
			print row[4]
			print row[5]
			print row[6] 
			print row[7]
			print row[8]
			print row[9]
			print row[10]