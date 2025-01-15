def xor_even_odd(T, test_cases):
    for _ in range(T):
        L, R = test_cases[_]
        xor = 0
        for i in range(L, R + 1):
            xor ^= i
        if xor % 2 == 0:
            print("Even")
        else:
            print("Odd")

T = int(input())
test_cases = []
for _ in range(T):
    L, R = map(int, input().split())
    test_cases.append((L, R))

xor_even_odd(T, test_cases)