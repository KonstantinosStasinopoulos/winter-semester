file=input('Enter file name:\n')
x=open(file,'rt',encoding='UTF8')
text=x.read()
list=[]


for c in text:
    list.append(ord(c))

for c in range(len(list)):
    list[c]=128-list[c]

for c in range(len(list)):
    list[c]=chr(list[c])

print(list)

for c in list:
    print(c[::-1],end=" ")



x.close()
