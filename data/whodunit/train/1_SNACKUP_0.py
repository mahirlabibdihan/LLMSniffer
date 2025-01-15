t = int(input())

for i in range(t):
    n = int(input())
    s = range(1, n + 1)
    print(n)
    for j in range(1, n + 1):
        print(n)
        for k in range(1, n + 1):
            print(k, s[(j + k - 1) % n], s[(j + k) % n])