def can_chef_get_out(T, scenarios):
    results = []
    for i in range(T):
        N, M = scenarios[i]
        if N*M % 2 == 0:
            results.append("Yes")
        else:
            results.append("No")
    return results

T = int(input())
scenarios = []
for _ in range(T):
    scenarios.append(list(map(int, input().split())))
results = can_chef_get_out(T, scenarios)
for result in results:
    print(result)