def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    min_a = min(a)
    max_a = max(a)
    queries = [int(input()) for _ in range(q)]
    results = ["Yes" if min_a <= t <= max_a else "No" for t in queries]
    print("\n".join(results))

solve()