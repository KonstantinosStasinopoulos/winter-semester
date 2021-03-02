import random
n=int(input("Enter the rectangle's length: \n"))
m=int(input("Enter the rectangle's width: \n"))
sos=[]

for i in range(n):
    sos.append([])
    for k in range(m):
        sos[i].append('')


poscount=n*m
list=[]
for i in range(poscount):
    list.append(i)

random.shuffle(list)

s=list[:(poscount//2+1)]
o=list[(poscount//2+1):]


for l in range(n):
    while('' in sos[l]):
        temp=0
        for i in range(n):
            for j in range(m):
                if(temp in s):
                    sos[i][j]='s'
                elif(temp in o):
                    sos[i][j]='o'

                temp=temp+1



cnt=0
for i in range(n):
    for j in range(m-2):
        if (sos[i][j]=='s' and sos[i][j+1]=='o' and sos[i][j+2]=='s'):
            cnt=cnt+1


for i in range(n-2):
    for j in range(m):
        if (sos[i][j]=='s' and sos[i+1][j]=='o' and sos[i+2][j]=='s'):
            cnt=cnt+1

for i in range(n-2):
    for j in range(m-2):
        if (sos[i][j]=='s' and sos[i][j+1]=='o' and sos[i+2][j+2]=='s'):
            cnt=cnt+1

for i in range(n-2):
    for j in range(2,m):
        if (sos[i][j]=='s' and sos[i+1][j-1]=='o' and sos[i+2][j-2]=='s'):
            cnt=cnt+1


print('the count is: ',cnt)
