n1,n2,n3=map(int,input().split())
l1=[]
l2=[]
l3=[]
for i in range(n1):
    l1.append(int(input()))
for i in range(n2):
    l2.append(int(input()))
for i in range(n3):
    l3.append(int(input()))
a = set(l1)
b = set(l2)
c = set(l3)
i1 = a & b
i2 = b & c
i3 = a & c

i1= i1.union(i2)
fr= list(i1.union(i3))
fr.sort()
print(len(fr))
for i in fr:
    print(i)
    