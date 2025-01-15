def min_sum_of_stones(T, test_cases):
    for i in range(T):
        n1, n2, m = test_cases[i]
        total = min(n1, n2, m*(m+1)//2)
        print(n1 + n2 - 2*total)

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(list(map(int, input().split())))

min_sum_of_stones(T, test_cases)