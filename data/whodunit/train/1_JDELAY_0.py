t=int(input())
while(t):
    n=int(input())
    c=0
    while(n):
        a,b=map(int,input().split())
        if b-a>5:
            c+=1
        n-=1
    print(c)
    t-=1
