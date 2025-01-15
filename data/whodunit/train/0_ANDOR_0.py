T = int(input().strip())
for _ in range(T):
    x = int(input().strip())
    if x % 2 == 0:
        print(x // 2, x // 2)
    else:
        print(0, x)