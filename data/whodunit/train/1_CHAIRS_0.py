t = int(input())
for m in range(t):
    n = int(input())
    sit = input()
    num0=0
    total=0
    max0=0
    s=0
    e=0
    i = 0
    while i < n:
        num0 = 0
        while i < n and sit[i] =="0":
            i += 1
            num0 += 1
        total+=num0
        if num0 > max0:
            max0 = num0
        if num0 == i:
            s = num0
        if i == n:
            e = num0
        i += 1
    if s+e>max0:
        max0=s+e
    print(total-max0)
