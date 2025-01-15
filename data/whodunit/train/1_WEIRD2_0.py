from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    c=Counter(l)
    cnt=0
    for i in c:
        curr=c[i]
        for j in range(1,c[i]+1):
            if c[j]>=i:
                if i==j:
                    cnt+=1 
                else:
                    cnt+=1
    print(cnt)