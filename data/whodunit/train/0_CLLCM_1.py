T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print("YES" if all(a & 1 for a in A) else "NO")