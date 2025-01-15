def find_freeze_time(T, test_cases):
    for _ in range(T):
        N, sensors = test_cases[_]
        readings = [0] * max(sensors)
        for i in range(N):
            for j in range(sensors[i]-1, len(readings), sensors[i]):
                if readings[j] == 1:
                    print(j+1)
                    break
                readings[j] = 1
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