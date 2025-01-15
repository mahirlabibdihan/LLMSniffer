def solve(n, k):
    if k>n-k:
        k=n-k
    res=1
    for i in range(k):
        res=res*(n-i)//(i+1)
    return res

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    print(solve(n, k))