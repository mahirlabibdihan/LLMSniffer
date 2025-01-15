def min_grass(T, test_cases):
    for _ in range(T):
        n, D = test_cases[_]
        villagers = []
        dinosaurs = []
        for i in range(n):
            if D[i] >= 0:
                villagers.append((D[i], i))
            else:
                dinosaurs.append((-D[i], i))
        villagers.sort(reverse=True)
        dinosaurs.sort(reverse=True)
        grass = 0
        while villagers and dinosaurs:
            laddus = min(villagers[-1][0], dinosaurs[-1][0])
            grass += laddus * abs(villagers[-1][1] - dinosaurs[-1][1])
            if villagers[-1][0] == laddus:
                villagers.pop()
            else:
                villagers[-1] = (villagers[-1][0] - laddus, villagers[-1][1])
            if dinosaurs[-1][0] == laddus:
                dinosaurs.pop()
            else:
                dinosaurs[-1] = (dinosaurs[-1][0] - laddus, dinosaurs[-1][1])
        print(grass)

T = int(input())
test_cases = []
for _ in range(T):
    n = int(input())
    D = list(map(int, input().split()))
    test_cases.append((n, D))
min_grass(T, test_cases)