n, m = map(int, input().split())
digits = list(map(int, list(input().strip())))
steps = [int(input()) for _ in range(m)]

for step in steps:
    x = digits[step - 1]
    B1 = sum([i - x for i in digits if i > x])
    B2 = sum([x - i for i in digits if i < x])
    print(B1 - B2)