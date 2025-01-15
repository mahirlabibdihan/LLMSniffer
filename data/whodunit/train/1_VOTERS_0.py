from collections import Counter
n1,n2,n3=map(int,input().split())
p=0
k,s=[],[]
for _ in range(n1+n2+n3):
    l=int(input())
    s.append(l)
t=Counter(s)
for x,y in t.items():
    if y>=2:
        p+=1
        k.append(x)
k.sort()
print(p)
for item in k:
    print(item)