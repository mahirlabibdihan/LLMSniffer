def solve(x):
    if x % 2 == 0:
        return x // 2, x // 2
    else:
        return 0, x

T = int(input().strip())
for _ in range(T):
    x = int(input().strip())
    a, b = solve(x)
    print(a, b)