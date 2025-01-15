def F(x):
    while x > 9:
        x = sum(map(int, str(x)))
    return x

def solve(A1, D, L, R):
    return sum(F(A1 + D * (i - 1)) for i in range(L, R + 1))

T = int(input().strip())
for _ in range(T):
    A1, D, L, R = map(int, input().strip().split())
    print(solve(A1, D, L, R))