for _ in range(int(input())):
    n=int(input())
    m=list(map(int,input().split()))
    a=0
    c=0
    for i in range(n):
        b=m[i]-c
        if b>=0:
            a+=b
            c+=b
        else:
            c+=b
    print(a)
