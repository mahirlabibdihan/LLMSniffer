try:
    for _ in range(int(input())):
        n,p,q = map(int,input().split())
        a = list(map(int,input().split()))
        a.sort()
        b = 0
        for i in a:
            if i//2 <= q and i%2 <= p:
                q -= i//2
                p -= i%2
                b+=1
            elif i//2 > q and i-2*q <= p:
                p -= i-2*q
                q = 0
                b += 1
        print(b)
except:
    pass
        