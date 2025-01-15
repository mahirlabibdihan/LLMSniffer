T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    i = 0
    while i < N:
        j = i
        while j < N - 1 and A[j] + 1 == A[j + 1]:
            j += 1
        if i == j:
            print(A[i], end='')
        elif i + 1 == j:
            print(A[i], A[j], sep=',', end='')
        else:
            print(A[i], A[j], sep='...', end='')
        if j < N - 1:
            print(',', end='')
        i = j + 1
    print()