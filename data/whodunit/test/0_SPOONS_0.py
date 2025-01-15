import math
import bisect

def min_cities(T, spoons):
    max_spoons = max(spoons)
    cities = [1]
    i = 1
    while cities[-1] < max_spoons:
        i += 1
        cities.append(cities[-1] + i)
    for spoon in spoons:
        print(bisect.bisect_left(cities, spoon) + 1)

T = int(input())
spoons = [int(input()) for _ in range(T)]
min_cities(T, spoons)