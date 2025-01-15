for i in range(int(input())):
    x=int(input())
    a=list(map(int,input().split()))
    b=set(a)
    b=list(b)
    b.sort()
    l=0
    for j in range(len(b)):
        if b[j]>x:
            break
        else:
            l=l+1
    print(x-l)
