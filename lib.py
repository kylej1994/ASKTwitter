import nltk
from nltk.corpus import cmudict
d=cmudict.dict()
def remPunc(x):
	ret=""
	for c in x:
		if(c.isalpha()or isdigit(c)):
			ret=ret+c
	return ret.lower()

def isdigit(c):
	digs=['1','2','3','4','5','6','7','8','9','0']
	return c in digs

def getSylls(word):
	if(word in d):
		return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word]][0]
	else:
		return 2

def readDict(f):
	diction={}
	fd=open(f, 'r')
	for line in fd:
		line=line[:len(line)-1]
		pos=line.index(" ")
		key=line[:pos]
		val=line[pos+1:]
		diction[key]=val
	return diction
