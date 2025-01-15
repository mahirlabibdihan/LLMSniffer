T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    x, y = 0, 0
    prev = ''
    for i in S:
        if (i in ['L', 'R']) and (prev in ['U', 'D', '']):
            x += 1 if i == 'R' else -1
            prev = i
        elif (i in ['U', 'D']) and (prev in ['L', 'R', '']):
            y += 1 if i == 'U' else -1
            prev = i
    print(x, y)