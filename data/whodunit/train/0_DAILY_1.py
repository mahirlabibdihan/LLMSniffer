def count_ways(X, N, cars):
    ways = 0
    for car in cars:
        compartments = [car[i*6:i*6+4] + car[54-i*2-1:56-i*2-1] for i in range(9)]
        ways += sum(compartment.count('0') >= X for compartment in compartments)
    return ways

X, N = map(int, input().split())
cars = [input() for _ in range(N)]
print(count_ways(X, N, cars))