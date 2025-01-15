t = int(input())
for _ in range(t):
    k = int(input())
    leaves = list(map(int, input().split()))
    stems = 1
    for i in range(k):
        if stems < leaves[i]:
            print('No')
            break
        stems = stems - leaves[i]
        stems *= 2
    else:
        if stems == 0:
            print('Yes')
        else:
            print('No')