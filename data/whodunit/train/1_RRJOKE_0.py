for _ in range(int(input())):
    n=int(input())
    for i in range(n) :
        x, y=map(int,input().split())
    p=0
    for i in range(1,n+1):
        p=p^i
    print(p) 
        