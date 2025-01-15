from itertools import product

def dish_ingredients(T, test_cases):
    for i in range(T):
        N, K, L = test_cases[i]
        dishes = list(product(range(1, K+1), repeat=N))
        dishes.sort()
        print(' '.join(map(str, dishes[L-1])))

T = int(input())
test_cases = []
for _ in range(T):
    N, K, L = map(int, input().split())
    test_cases.append((N, K, L))
dish_ingredients(T, test_cases)