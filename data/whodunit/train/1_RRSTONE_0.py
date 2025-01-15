n,k = map(int,input().split())
list1 = list(map(int,input().split()))
maxx = max(list1)
if k==0:
    pass
elif k!=0 and k%2!=0:
    for i in range(n):
        list1[i]=maxx-list1[i]
else:
    for i in range(n):
        list1[i]= maxx-list1[i]
    maxx2 = max(list1)
    for i in range(n):
        list1[i]=maxx2-list1[i]
for val in list1:
    print(val,end=" ")
    
