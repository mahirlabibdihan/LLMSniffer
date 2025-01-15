def is_fair_order(T, test_cases):
    for _ in range(T):
        N, M, A = test_cases[_]
        counter = [0]*N
        for cat in A:
            counter[cat-1] += 1
            if max(counter) > min(counter) + 1:
                print("NO")
                break
        else:
            print("YES")

T = int(input())
test_cases = []
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append((N, M, A))
is_fair_order(T, test_cases)