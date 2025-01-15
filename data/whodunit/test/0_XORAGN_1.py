def xor_sequence(T, test_cases):
    for _ in range(T):
        N = test_cases[_][0]
        A = test_cases[_][1]
        xor_B = 0
        for i in range(N):
            for j in range(N):
                xor_B ^= A[i] + A[j]
        print(xor_B)

T = int(input().strip())
test_cases = []
for _ in range(T):
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    test_cases.append((N, A))
xor_sequence(T, test_cases)