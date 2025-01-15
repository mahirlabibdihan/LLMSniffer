for _ in range(int(input())):
    m, b = map(int, input().split())
    while m != 0:
        m, b = b%m, m
    print(2*b)