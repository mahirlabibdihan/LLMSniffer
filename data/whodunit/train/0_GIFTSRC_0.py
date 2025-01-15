T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    x, y = 0, 0
    prev = ''
    for i in S:
        if (i == 'L' or i == 'R') and (prev == 'U' or prev == 'D' or prev == ''):
            if i == 'L':
                x -= 1
            else:
                x += 1
            prev = i
        elif (i == 'U' or i == 'D') and (prev == 'L' or prev == 'R' or prev == ''):
            if i == 'U':
                y += 1
            else:
                y -= 1
            prev = i
    print(x, y)