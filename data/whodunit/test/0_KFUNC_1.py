def F(x):
    if x < 10:
        return x
    else:
        return F(sum(int(digit) for digit in str(x)))

def solve(A1, D, L, R):
    return sum(F(A1 + D * (i - 1)) for i in range(L, R + 1))

T = int(input().strip())
for _ in range(T):
    A1, D, L, R = map(int, input().strip().split())
    print(solve(A1, D, L, R))