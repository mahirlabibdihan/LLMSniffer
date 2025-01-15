def max_power(N, m, c, houses):
    village1, village2 = 0, 0
    for house in houses:
        x, y, p = house
        if y > m * x + c:
            village1 += p
        else:
            village2 += p
    return max(village1, village2)

N = int(input())
m, c = map(int, input().split())
houses = [list(map(int, input().split())) for _ in range(N)]
print(max_power(N, m, c, houses))