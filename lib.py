def remPunc(x):
	ret=""
	for c in x:
		if(c.isalpha()):
			ret=ret+c
	return ret.lower()

def isVowel(c):
	if((c=='a')or(c=='e')or(c=='i')or(c=='o')or(c=='u')):
		return True
	else:
		return False

def isNotE(c):
	return (isVowel(c)and(not(c=='e'))

def getSylls(word):
	i=0
	count=0
	while(i<range(len(word))):
		if(i==len(word-1)):
			if(isNotE(word[i])):
				count+=1
				break
			break
		elif(isVowel(word[i])and(isVowel(word[i+1])):
			word=word[:i]+word[i+1:]
		elif(word[i]=='e'):
			if(not(i==len(word)-1)):
				count+=1
		elif(isVowel(word[i])):
			count+=1
		elif(word[i]=='y'):
			if(i==0):
				if(len(word)==1):
					count+=1
					break
				elif(not(isVowel(word[i+1]))):
					count+=1
			else:
				if(i==len(word)-1):
					if(not(isVowel(word[i-1]))):
						count+=1
