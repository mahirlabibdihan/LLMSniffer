def solve(n):
    if n == 1:
        return 1
    elif n == 2:
        return 4
    elif n == 3:
        return 12
    else:
        return 24 * pow(n - 3, 5) + 96 * pow(n - 3, 4) + 72 * pow(n - 3, 3) + 12 * pow(n - 3, 2)

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(solve(N))