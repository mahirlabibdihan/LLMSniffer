T = int(input())
for _ in range(T):
    N = int(input())
    directions = [input() for _ in range(N)]
    directions = directions[::-1]
    for i in range(len(directions)):
        if i == 0:
            print('Begin ' + ' '.join(directions[i].split()[2:]))
        elif 'Left' in directions[i]:
            print('Right ' + ' '.join(directions[i].split()[2:]))
        else:
            print('Left ' + ' '.join(directions[i].split()[2:]))
    print()