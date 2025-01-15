def xor_even_odd(T, test_cases):
    for _ in range(T):
        L, R = test_cases[_]
        if ((R - L) % 2 == 0 and R % 2 == 0) or ((R - L) % 2 == 1 and L % 2 == 0):
            print("Even")
        else:
            print("Odd")

T = int(input())
test_cases = []
for _ in range(T):
    L, R = map(int, input().split())
    test_cases.append((L, R))

xor_even_odd(T, test_cases)