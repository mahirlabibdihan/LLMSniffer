def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    min_a = min(a)
    max_a = max(a)
    for _ in range(q):
        t = int(input())
        if min_a <= t <= max_a:
            print("Yes")
        else:
            print("No")

solve()