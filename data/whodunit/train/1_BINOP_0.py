t = int(input())

for i in range(t):
    a = input()
    b = input()
    n = len(a)
    z, o = 0, 0
    for j in a:
        if j == '0':
            z = 1 
        else:
            o = 1
    if z == 0 or o == 0:
        print('Unlucky Chef')
    else:
        n1, n2 = 0, 0
        for j in range(n):
            e = a[j]
            if e == '1' and e != b[j]:
                n1 += 1
            elif e == '0' and e != b[j]:
                n2 += 1
        print('Lucky Chef')
        ans = max(n1, n2)
        print(ans) 