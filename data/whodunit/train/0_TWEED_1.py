def winner(T, test_cases):
    for _ in range(T):
        N, P, heaps = test_cases[_]
        if P == "Dee" and max(heaps) % 2 == 0:
            print("Dee")
        else:
            print("Dum")

T = int(input().strip())
test_cases = []
for _ in range(T):
    N, P = input().strip().split()
    N = int(N)
    heaps = list(map(int, input().strip().split()))
    test_cases.append((N, P, heaps))
winner(T, test_cases)