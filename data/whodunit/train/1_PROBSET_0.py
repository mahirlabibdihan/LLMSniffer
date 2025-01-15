for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = 'FINE'
    temp = ''
    for _ in range(n):
        a, b = input().split()
        if a == 'correct' and b.count('0') > 0:
            ans = 'INVALID'
        elif a == 'wrong' and b.count('0') == 0:
            temp = 'WEAK'
    if ans == 'FINE' and len(temp) > 0: print(temp)
    else:
        print(ans)