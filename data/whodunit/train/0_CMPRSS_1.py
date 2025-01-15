T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    i = 0
    result = []
    while i < N:
        j = i
        while j < N - 1 and A[j] + 1 == A[j + 1]:
            j += 1
        if i == j:
            result.append(str(A[i]))
        elif i + 1 == j:
            result.append(str(A[i]))
            result.append(str(A[j]))
        else:
            result.append(str(A[i]) + '...' + str(A[j]))
        i = j + 1
    print(','.join(result))