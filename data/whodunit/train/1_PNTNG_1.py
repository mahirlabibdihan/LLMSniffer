n,m,h = map(int, input().split())
numCells = n * m
tk_ck = []
tot=0
for _ in range(h):
    t,c = map(int, input().split())
    tk_ck.append((t,c))
    tot+=t
if tot < numCells:
    print('Impossible')
else:
    tk_ck = sorted(tk_ck, key=lambda x:x[1])
    curCost = 0
    i = 0
    while numCells > 0:
        curCost += tk_ck[i][1] * min(tk_ck[i][0], numCells)
        numCells -= tk_ck[i][0]
        i += 1
    print(curCost)