def min_stops(n, m, houses):
    houses.sort()
    min_stops = float('inf')
    for x in range(1, n+1):
        stops = 0
        for i in range(m):
            stops += (houses[i]-1)//x + 1
        min_stops = min(min_stops, stops)
    return min_stops

n, m = map(int, input().split())
houses = list(map(int, input().split()))
print(min_stops(n, m, houses))