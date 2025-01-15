def max_digit_sum(T, test_cases):
    for _ in range(T):
        N, A = test_cases[_]
        max_sum = 0
        for i in range(N-1):
            for j in range(i+1, N):
                product = A[i]*A[j]
                digit_sum = sum(int(digit) for digit in str(product))
                if digit_sum > max_sum:
                    max_sum = digit_sum
        print(max_sum)

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append((N, A))
max_digit_sum(T, test_cases)