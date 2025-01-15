from collections import Counter
l=[]
for _ in range(int(input())):
    s=input().strip()
    l.append(s)
s=Counter(l[0])
for i in range(1,len(l)):
    s=s&Counter(l[i])
s=list(s.elements())
if(len(s)!=0):
    print(*sorted(s),sep='')
else:
    print("no such string")
    
            