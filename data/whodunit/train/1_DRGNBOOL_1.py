
t = int(input())
while t:
    n,m = map(int, input().split())
    soints = {}
    sofloats = {}
    while n:
        c,l = map(int, input().split())
        if l in soints.keys():
            soints[l] += c
        else:
            soints[l] = c
        n -= 1
    while m:
        c,l = map(int, input().split())
        if l in sofloats.keys():
            sofloats[l] += c
        else:
            sofloats[l] = c
        m -= 1
    c = 0
    for l in soints.keys():
        if sofloats[l]>=soints[l]:
            c += sofloats[l]-soints[l]
    print(c)
    t -= 1
