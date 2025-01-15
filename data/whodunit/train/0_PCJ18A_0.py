T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    if any(a >= X for a in A):
        print("YES")
    else:
        print("NO")