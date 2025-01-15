for _ in range(int(input())):
    n=int(input())
    a=input()
    c=input()
    w=list(map(int,input().split()))
    j=0
    for i in range(n):
        if a[i]==c[i]:
            j+=1
    if n==j:
        print(w[-1])
    else:
        print(max(w[:j+1]))