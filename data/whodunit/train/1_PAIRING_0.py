t = int(input())

for j in range(t):

    n, m = map(int, input().split())

    nlist = [i for i in range(n)]
    mlist = []

    for i in range(m):
        mlist.append(tuple(map(int, input().split())))

    mlist2 = mlist.copy()

    mlist.reverse()

    mselected = []

    for (x,y) in mlist:
        if x in nlist and y in nlist:
            nlist.remove(x)
            nlist.remove(y)
            mselected.append(mlist2.index((x,y)))


    p = ''
    for i in mselected:
        p = str(i) + ' ' + p

    print(p)