def solve(N):
    if N == 1:
        return 'y y y'
    elif N == 2:
        return 'n y y'
    else:
        return 'n y n'

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(solve(N))