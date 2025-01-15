def max_xor():
    T = int(input())
    for _ in range(T):
        N, A, B = map(int, input().split())
        ones = bin(A)[2:].count('1') + bin(B)[2:].count('1')
        ones = min(ones, N)
        zeros = N - ones
        result = '1'*ones + '0'*zeros
        print(int(result, 2))

max_xor()