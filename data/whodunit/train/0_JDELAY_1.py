T = int(input())
for _ in range(T):
    N = int(input())
    submissions = [list(map(int, input().split())) for _ in range(N)]
    print(sum(1 for S, J in submissions if J - S > 5))