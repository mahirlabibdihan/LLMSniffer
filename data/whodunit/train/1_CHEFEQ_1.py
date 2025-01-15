for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    d = {}
    for i in l:
        try:
            d[i]+=1
        except:
            d.setdefault(i,1)
    m = 0
    for i in d.values():
        if m<i:
            m = i
    print(n-m)