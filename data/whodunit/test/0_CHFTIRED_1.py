def solve(a, b):
    return "YES" if abs(a - b) % 2 == 0 else "NO"

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(solve(a, b))