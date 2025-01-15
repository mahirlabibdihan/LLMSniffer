T = int(input())
for _ in range(T):
    A = int(input())
    D1 = A.bit_length() - 1
    D2 = max(D1, A.bit_length() - 2)
    print(D1, D2)