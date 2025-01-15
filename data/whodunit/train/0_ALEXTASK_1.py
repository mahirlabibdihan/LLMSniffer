def find_freeze_time(T, test_cases):
    for _ in range(T):
        N, sensors = test_cases[_]
        readings = set()
        for i in range(N):
            for j in range(sensors[i], max(sensors)+1, sensors[i]):
                if j in readings:
                    print(j)
                    break
                readings.add(j)
            else:
                continue
            break

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    sensors = list(map(int, input().split()))
    test_cases.append((N, sensors))
find_freeze_time(T, test_cases)