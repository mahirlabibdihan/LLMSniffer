t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l=list(set(l))
    l.sort()
    a=l[len(l)-1]
    b=l[len(l)-2]
    print(b%a)