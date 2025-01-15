def solve(t1, t2, t3, t4):
    total = t1 + t2 + t3
    if total == 0:
        return 0.0
    else:
        return t1 / total

T = int(input())
for _ in range(T):
    t1, t2, t3, t4 = map(int, input().split())
    print("{:.6f}".format(solve(t1, t2, t3, t4)))