def F(A):
    while A >= 10:
        A = sum(int(i) for i in str(A))
    return A

T = int(input().strip())
for _ in range(T):
    A, N = map(int, input().strip().split())
    if A < 10:
        print(A)
    elif N == 1:
        print(F(A))
    elif A % 5 == 0:
        print(5)
    else:
        print(1)