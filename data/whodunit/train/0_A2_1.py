def is_possible(leaves, k):
    stems = 1
    for i in range(k):
        if stems < leaves[i]:
            return 'No'
        stems = stems - leaves[i]
        stems *= 2
    return 'Yes' if stems == 0 else 'No'

t = int(input())
for _ in range(t):
    k = int(input())
    leaves = list(map(int, input().split()))
    print(is_possible(leaves, k))