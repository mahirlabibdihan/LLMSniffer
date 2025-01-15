# PythonBytes
from sys import stdin, stdout
 
for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    sets = {}
    ans = 0
    for c in range(n):
        inp = stdin.readline().split()
        inp.remove(inp[0])
        inp = frozenset(inp)
        if inp in sets.keys():
            sets[inp]+=1
        else:
            sets[inp]=1
    for x in sets.keys():
        if len(x)==k:
            ans+=sets[x]*(sets[x]-1)
    for a in sets.keys():
        for b in sets.keys():
            if a!=b and len(a.union(b))==k:
                ans+=sets[a]*sets[b]
    stdout.write("%d\n"%(ans//2)) 