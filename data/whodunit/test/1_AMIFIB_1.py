def bis(a,key,p,q):

    if q==p+1 and a[p]!=key:
        return False

    mid=(p+q)//2
    if a[mid]==key:
        return True
    if a[mid]<key:
        return bis(a,key,mid,q)
    else:
        return bis(a,key,p,mid)



query=[]
for _ in range(int(input())):
    query.append(int(input()))

maxi=max(query)

seq=[0,1]
while seq[-1]+seq[-2]<=maxi:
    seq.append(seq[-1]+seq[-2])

lens=len(seq)

for i in query:
    if bis(seq,i,0,lens):
        print("YES")
    else:
        print("NO")
