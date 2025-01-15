def calculate_probability(t1, t2, t3, t4):
    total_tickets = t1 + t2 + t3
    if total_tickets == 0:
        return 0.0
    else:
        return t1 / total_tickets

test_cases = int(input())
for _ in range(test_cases):
    t1, t2, t3, t4 = [int(x) for x in input().split()]
    print("{:.6f}".format(calculate_probability(t1, t2, t3, t4)))