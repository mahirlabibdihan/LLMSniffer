def isSubsetSum(set, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if set[n-1] > sum:
        return isSubsetSum(set, n-1, sum)
    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    banknotes = []
    for _ in range(N):
        banknotes.append(int(input()))
    if isSubsetSum(banknotes, N, M):
        print('Yes')
    else:
        print('No')