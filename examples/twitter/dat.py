import workshop

tweetfile='../../tweets.json'

mon={}

ls=workshop.get_tweets(tweetfile,100000)
for tw in ls:
    st=tw['created_at']
    ind=st.find(" ")+1
    mat=st[ind:ind+3]
    if(mat in mon):
        mon[mat]+=1
    else:
        mon[mat]=1

for key in mon:
    print(key+": "+str(mon[key]))


#print(ls[0]['created_at'])

