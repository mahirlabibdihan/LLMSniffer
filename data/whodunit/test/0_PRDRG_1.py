def solve(n):
    x = 1
    y = 2
    for i in range(n-1):
        if i%2 == 0:
            x, y = x+y, y
        else:
            x, y = x, x+y
    return x, y

T = int(input())
for _ in range(T):
    N = int(input())
    x, y = solve(N)
    print(x, y)