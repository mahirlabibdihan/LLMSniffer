T = int(input().strip())
for _ in range(T):
    s, n = input().strip().split()
    n = int(n)
    prefix_count = [0]
    for c in s:
        prefix_count.append(prefix_count[-1] + (1 if c == 'a' else -1))
    total = 0
    for i in range(1, len(prefix_count)):
        if prefix_count[i] > 0:
            total += 1
    total *= n
    if prefix_count[-1] > 0:
        total += prefix_count[-1] * (n * (n - 1)) // 2
    print(total)