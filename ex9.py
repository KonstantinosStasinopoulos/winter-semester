file=input('Enter file name:\n')
x=open(file,'rt',encoding='UTF8')
text=x.read()
list=[]
list2=[]
for c in text:
    if(ord(c)%2!=0):
        list.append(ord(c))



for i in list:
    if(65<=i<90 or 97<=i<122):
        list2.append(i)




list2.sort()
length=len(list2)
print(length)
for i in list2:
    cnt=0
    for k in list:
        if(i==k):
            cnt=cnt+1
            list2.remove(k)
    prc=cnt*100//length + 1
    temp=''
    for c in range(prc):
        temp='*'+temp
    print(chr(i),':',temp,'\n')


x.close()
