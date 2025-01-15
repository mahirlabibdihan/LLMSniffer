def findsubtract(num):
    n = num
    strn = str(n)
    count = 0
    while n > 0:
        fd = int(strn[0])
        p = len(strn) - 1
        if p == 0:
            n -= fd
            strn = str(n)
            count += 1
        else:
            n1 = n - fd * 10**p
            n2 = n1//fd+1
            count += n2
            n -= n2 * fd
            strn = str(n)
    return count + 1





for i in range(int(input())):
    k = int(input())
    if k == 2:
        print(9)
        continue
    n = None
    brutetop = 4 * k
    brutebottom = 0
    while abs(brutetop - brutebottom) > 20:
        v = round((brutetop + brutebottom) / 2)
        t = findsubtract(v)
        if t <= k:
            brutebottom = v
        else:
            brutetop = v
    for j in range(brutetop, brutebottom - 1, -1):
        n = findsubtract(j)
        if n == k:
            print(j)
            break
