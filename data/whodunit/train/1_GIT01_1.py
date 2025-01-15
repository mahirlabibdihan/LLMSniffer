def pat(pl,row):
    dict1 = {1:5,0:3}
    dict2 = {'R':1,'G':0}
    k=1
    c1=0
    c2=0
    for sl in pl:
        for e in sl:
            if dict2[e]!=k:
                c1+=dict1[abs(k-1)]
            else:
                c2+=dict1[k]
            k=abs(k-1)
        if row%2 == 0:
            k=abs(k-1)
    if c1<c2:
        return c1
    else:
        return c2

T = int(input())
for i in range(T):
    a,b = [int(x) for x in input().split()]
    costr = []
    for j in range(a):
        costr.append(input())
    print(pat(costr,b))