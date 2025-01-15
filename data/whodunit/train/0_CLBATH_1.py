def can_chef_take_bath(n, test_cases):
    for i in range(n):
        v1, t1, v2, t2, v3, t3 = test_cases[i]
        if t1 <= t3 <= t2 and v1 + v2 >= v3:
            if (v1 * t1 + v2 * t2) / (v1 + v2) == t3:
                print("YES")
                continue
        print("NO")

n = int(input())
test_cases = []
for _ in range(n):
    test_cases.append(list(map(int, input().split())))
can_chef_take_bath(n, test_cases)