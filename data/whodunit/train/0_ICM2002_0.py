T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    B = list(map(int, input().split()))
    B.sort()
    if all(x % K == B[0] % K for x in B):
        print("YES")
    else:
        print("NO")