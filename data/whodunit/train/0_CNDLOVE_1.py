def can_distribute_candies(T, test_cases):
    for i in range(T):
        N, A = test_cases[i]
        if sum(A) % 2 == 0 and max(A) <= sum(A) // 2:
            print("YES")
        else:
            print("NO")

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append((N, A))

can_distribute_candies(T, test_cases)