def min_operations(T, test_cases):
    for _ in range(T):
        A, B = test_cases[_]
        a = format(A, 'b').count('1')
        b = format(B, 'b').count('1')
        if a < b or B == 0 and A != 0:
            print(-1)
        else:
            print(max(1, b))

T = int(input())
test_cases = []
for _ in range(T):
    A, B = map(int, input().split())
    test_cases.append((A, B))
min_operations(T, test_cases)