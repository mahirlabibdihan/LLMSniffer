T = int(input())
for _ in range(T):
    S = input()
    total = 0
    for c in S:
        if c.isdigit():
            total += int(c)
    print(total)