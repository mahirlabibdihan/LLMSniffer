for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    l=sorted(l)
    for i in range(k):
        l.append(10001)
    print(l[(len(l)//2)])