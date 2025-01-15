for t in range(int(input())):
    n,a,b=map(int,input().split())
    a = bin(a)
    b = bin(b)
    ones = a.count('1') + b.count('1')
    num = 0
    l = abs(n - ones)
    for i in range(l, n):
        num += 2**i
    print(num)