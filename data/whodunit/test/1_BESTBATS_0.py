from itertools import combinations
for _ in range(int(input())):
    a=[int(x) for x in input().split()]
    k=int(input())
    a.sort(reverse=True)
    s=0
    for i in range(k):
        s+=a[i]
    z=list(combinations(a,k))
    c=0
    for i in z:
        if sum(i)==s:
            c+=1
    print(c)
            
    