T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print("YES" if max(A) >= X else "NO")