T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input())) for _ in range(N)]
    collisions = sum(max(0, sum(row) - 1) for row in zip(*matrix))
    print(collisions)