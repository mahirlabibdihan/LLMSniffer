for _ in range(int(input())):
    x=int(input())
    l=list(map(int,input().split()))
    if l.index(max(l))<l.index(min(l)):
        print(max(l),min(l))
    else:
        print(min(l),max(l))
