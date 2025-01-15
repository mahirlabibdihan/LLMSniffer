from fractions import Fraction
T = int(input())
for _ in range(T):
    N, A, K = map(int, input().split())
    X = A*N + (K-1)*((N-2)*180 - 2*A)
    Y = N
    result = Fraction(X, Y)
    print(result.numerator, result.denominator)