for _ in range(int(input())):
    n=int(input())
    a=int(n**0.5)
    s=0
    while a>0 and a*a>=n-700:
        s+=n-a*a
        a-=1
    print(a*700 +s)