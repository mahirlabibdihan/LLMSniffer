n = int(input())
l = list(map(int, input().split()))
m = []
for i in l:
    if i % 5 != 0:
        m.append(i)
    else:
        k = i
        p = i
        c1 = 0
        c2 = 0
        while k % 5 == 0:
            c1 += 1
            k //= 5
        while p % 2 == 0:
            c2 += 1
            p //= 2
        if c2 >= c1:
            m.append(i)
        else:
            m.append(i * (4 ** ((c1 - c2 + 1) // 2)))
for j in m:
    print(j, end = "\n")