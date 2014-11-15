from sys import stdin
import random
import string
import lib
import sys
dp={}
ws=[]
dc=lib.readDict(sys.argv[1])
seed=sys.argv[2]
for key in dc:
	for word in dc[key].split():
		ws.append(lib.remPunc(word))
	ws.append("END")
start=seed
for i in range(len(ws)):
	if(ws[i]=="END"):
		dp["END"]=["END"]
	elif(ws[i] in dp):
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
