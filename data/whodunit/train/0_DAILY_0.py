def count_ways(X, N, cars):
    ways = 0
    for car in cars:
        for i in range(9):
            free_places = car[i*6:i*6+4].count('0') + car[54-i*2-1:56-i*2-1].count('0')
            if free_places >= X:
                ways += 1
    return ways

X, N = map(int, input().split())
cars = [input() for _ in range(N)]
print(count_ways(X, N, cars))