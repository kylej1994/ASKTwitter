from sys import stdin
import random
import string
import lib
dp={}
ws=[]

for line in stdin:
	for word in line.split():
		word=lib.remPunc(word)
		ws.append(word)
ws.append("END")
start=ws[0]
for i in range(len(ws)):
	if(ws[i]=="END"):
		dp["END"]=["END"]
		break
	if(ws[i] in dp):
		dp[ws[i]].append(ws[i+1])
	else:
		dp[ws[i]]=[]
		dp[ws[i]].append(ws[i+1])
numsyls=random.randrange(8,10)
syl=0
while(not (start=="END")):
	print(start +" ",end="")
	syl+=lib.getSylls(start)
	if(syl>=numsyls):
		print("")
		syl=0
	i=random.randrange(0,len(dp[start]))
	start=dp[start][i]
	if(start=="END"):
		break
print("")
