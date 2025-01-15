T = int(input())
for _ in range(T):
    N, a, b, c = map(int, input().split())
    F = list(map(int, input().split()))
    times = [abs(f - b) + abs(a - f) + c for f in F]
    print(min(times))