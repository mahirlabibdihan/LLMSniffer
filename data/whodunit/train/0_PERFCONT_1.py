def is_contest_balanced(T, test_cases):
    for t in range(T):
        N, P, A = test_cases[t]
        cakewalk = len([i for i in A if i >= P//2])
        hard = len([i for i in A if i <= P//10])
        if cakewalk == 1 and hard == 2:
            print("yes")
        else:
            print("no")

T = int(input())
test_cases = []
for _ in range(T):
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append((N, P, A))
is_contest_balanced(T, test_cases)