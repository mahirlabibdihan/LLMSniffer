n, m = map(int, input().split())
digits = list(map(int, list(input().strip())))
steps = [int(input()) for _ in range(m)]

for step in steps:
    x = digits[step - 1]
    B1, B2 = 0, 0
    for i in digits:
        if i > x:
            B1 += i - x
        elif i < x:
            B2 += x - i
    print(B1 - B2)