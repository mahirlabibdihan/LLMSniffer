def digit_sum(n):
    return (n - 1) % 9 + 1 if n > 0 else 0

T = int(input().strip())
for _ in range(T):
    A, N = map(int, input().strip().split())
    if A < 10:
        print(A)
    elif N == 1:
        print(digit_sum(A))
    elif A % 5 == 0:
        print(5)
    else:
        print(1)