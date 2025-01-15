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
        i = j = 0
        grass = 0
        while i < len(villagers) and j < len(dinosaurs):
            laddus = min(villagers[i][0], dinosaurs[j][0])
            grass += laddus * abs(villagers[i][1] - dinosaurs[j][1])
            villagers[i] = (villagers[i][0] - laddus, villagers[i][1])
            dinosaurs[j] = (dinosaurs[j][0] - laddus, dinosaurs[j][1])
            if villagers[i][0] == 0:
                i += 1
            if dinosaurs[j][0] == 0:
                j += 1
        print(grass)

T = int(input())
test_cases = []
for _ in range(T):
    n = int(input())
    D = list(map(int, input().split()))
    test_cases.append((n, D))
min_grass(T, test_cases)