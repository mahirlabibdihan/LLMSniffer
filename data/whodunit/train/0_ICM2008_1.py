def can_meet(T, test_cases):
    for i in range(T):
        a, b, c, d = test_cases[i]
        if (b - a) % (c + d) == 0:
            print("YES")
        else:
            print("NO")

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(list(map(int, input().split())))
can_meet(T, test_cases)