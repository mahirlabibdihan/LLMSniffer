def dish_ingredients(T, test_cases):
    for i in range(T):
        N, K, L = test_cases[i]
        dish = [1]*N
        for _ in range(L-1):
            for j in range(N-1, -1, -1):
                if dish[j] < K:
                    dish[j] += 1
                    break
                else:
                    dish[j] = 1
        print(' '.join(map(str, dish)))

T = int(input())
test_cases = []
for _ in range(T):
    N, K, L = map(int, input().split())
    test_cases.append((N, K, L))
dish_ingredients(T, test_cases)