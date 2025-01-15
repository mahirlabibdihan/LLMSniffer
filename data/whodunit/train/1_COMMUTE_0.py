for _ in range(int(input())):
    n=int(input())
    s=0
    for i in range(n):
        x,l,f=map(int,input().split())
        while s>x:
            x+=f
        s=x+l
    print(s)
                