def find_M(N):
    if N == 1:
        return 0
    elif N & (N + 1) == 0:
        return N // 2
    else:
        return -1

T = int(input())
for _ in range(T):
    N = int(input())
    print(find_M(N))