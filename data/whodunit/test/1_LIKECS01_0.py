for _ in range(int(input())):
    s = str(input())
    l = ''
    for i in s:
        if i not in l:
            l = l + i
    if len(s) == len(l):
        print('no')
    else:
        print('yes')