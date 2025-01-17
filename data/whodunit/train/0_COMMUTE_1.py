def min_time_to_reach_destination(T, test_cases):
    for _ in range(T):
        n = test_cases[_][0]
        schedules = test_cases[_][1]
        time = 0
        for i in range(n):
            x, l, f = schedules[i]
            while time < x or time % f != 0:
                time += 1
            time += l
        print(time)

T = int(input())
test_cases = []
for _ in range(T):
    n = int(input())
    schedules = []
    for _ in range(n):
        x, l, f = map(int, input().split())
        schedules.append((x, l, f))
    test_cases.append((n, schedules))

min_time_to_reach_destination(T, test_cases)