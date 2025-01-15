T = int(input())            # Test Cases
def func():
    global uni ,extra, c
    if len(uni) > 3:
        if len(uni) == 4 or len(uni) == 5:
            extra += len(uni) - 3
        else:
            extra += 4
        for i in uni:
            c.remove(i)
        uni = set(c[1:])
        func()
for i in range(T):
    n = int(input())        # No. of players
    points = []
    for k in range(n):
        c = list(map(int, input().split()))  # cookies data
        uni = set(c[1:])   # unique cookies data
        extra = c[0]
        func()
        points.append(extra)
    if points.count(max(points)) > 1:print('tie')
    elif points.index(max(points)) == 0:print('chef')
    else: print(points.index(max(points)) + 1)
