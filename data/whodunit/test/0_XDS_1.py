def print_string(N):
    if N == 1:
        return 'XD'
    else:
        return 'X' + 'D' * N

T = int(input())
for _ in range(T):
    N = int(input())
    print(print_string(N))