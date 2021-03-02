import tweepy

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")


api = tweepy.API(auth)

user=input("Enter Account Name: \n")



timeline = api.user_timeline(user)
i=1
words=[]
length=[]


for tweet in timeline:
    if(i>10):
        break
    tweet=tweet.text.split()
    for word in tweet:                                               #Αφαιρούμε όλους τους χαρακτήρες εκτός απο τα γράμματα και την απόστροφο
        newword=word
        for char in word:
            if (not(90>=ord(char)>=65 or 122>=ord(char)>=97 or char=="'")):
                newword=word.replace(char,'')
                word=newword

        words.append(word)
        length.append(len(word))

    i=i+1


l=len(words)
for i in range(1,l-1):
    for j in range(l-1,i-1,-1):
        if (length[j]>length[j-1]):
            length[j],length[j-1]=length[j-1],length[j]
            words[j],words[j-1]=words[j-1],words[j]





print('The 5 longest words are: \n')
for i in range(5):  print(words[i])
print('\n')
print('The 5 sortest words are: \n')
for i in range(l,l-5,-1): print(words[i-1])
