T = int(input())
for _ in range(T):
    N = int(input())
    directions = [input().split() for _ in range(N)]
    directions = directions[::-1]
    for i in range(len(directions)):
        if i == 0:
            print('Begin ' + ' '.join(directions[i][2:]))
        elif 'Left' == directions[i][0]:
            print('Right ' + ' '.join(directions[i][2:]))
        else:
            print('Left ' + ' '.join(directions[i][2:]))
    print()