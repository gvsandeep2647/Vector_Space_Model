import nltk
#from inverted.py import create_index
sentence1 = "Lorem ipsum dolor sit amet, Lorem adipiscing elit."
sentence2 = "Cur id non ita Lorem Beatus autem esse in maximarum rerum timore nemo potest."
sentence3 = "Quid est igitur, inquit, quod requiras?"
sentence4 = "Nam bonum ex quo appellatum sit, nescio, praepositum ex eo credo,"
forindex1 = set()
forindex1 = sentence1.split() + sentence2.split() + sentence3.split() + sentence4.split() 

def position_index(placeholder):
	position = {}
	for word in placeholder:
		position[word] = {}
		if sentence1.find(word)>=0:
			position[word]['sentence1'] = []
			for n in xrange(len(sentence1)):
				if sentence1.find(word,n)>=0:
					position[word]['sentence1'].append(sentence1.find(word,n)) 
			position[word]['sentence1'] = list(set(position[word]['sentence1']))
		if sentence2.find(word)>=0:
			position[word]['sentence2'] = []
			for n in xrange(len(sentence1)):
				if sentence2.find(word,n)>=0:
					position[word]['sentence2'].append(sentence2.find(word,n)) 
			position[word]['sentence2'] = list(set(position[word]['sentence2']))
		if sentence3.find(word)>=0:
			position[word]['sentence3'] = []
			for n in xrange(len(sentence1)):
				if sentence3.find(word,n)>=0:
					position[word]['sentence3'].append(sentence3.find(word,n)) 
			position[word]['sentence3'] = list(set(position[word]['sentence3']))
		if sentence4.find(word)>=0:
			position[word]['sentence4'] = []
			for n in xrange(len(sentence1)):
				if sentence4.find(word,n)>=0:
					position[word]['sentence4'].append(sentence4.find(word,n)) 
			position[word]['sentence4'] = list(set(position[word]['sentence4']))
	print position
#print forindex1
#print forindex1
position_index(forindex1)
