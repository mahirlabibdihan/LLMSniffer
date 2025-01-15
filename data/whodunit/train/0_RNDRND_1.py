def min_stops(n, m, houses):
    houses.sort()
    stops = [0]*(n+1)
    for x in range(1, n+1):
        for i in range(m):
            stops[x] += (houses[i]-1)//x + 1
    return min(stops)

n, m = map(int, input().split())
houses = list(map(int, input().split()))
print(min_stops(n, m, houses))