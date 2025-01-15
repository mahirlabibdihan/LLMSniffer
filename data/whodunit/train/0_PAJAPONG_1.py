def who_serves_next(T, test_cases):
    for i in range(T):
        X, Y, K = test_cases[i]
        if ((X + Y) // K) % 2 == 0:
            print("Chef")
        else:
            print("Paja")

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(list(map(int, input().split())))
who_serves_next(T, test_cases)