T = int(input())
for _ in range(T):
    N = int(input())
    late_submissions = 0
    for _ in range(N):
        S, J = map(int, input().split())
        if J - S > 5:
            late_submissions += 1
    print(late_submissions)