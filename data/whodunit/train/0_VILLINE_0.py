N = int(input())
m, c = map(int, input().split())
village1, village2 = 0, 0
for _ in range(N):
    x, y, p = map(int, input().split())
    if y > m * x + c:
        village1 += p
    else:
        village2 += p
print(max(village1, village2))