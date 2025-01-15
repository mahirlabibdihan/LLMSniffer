T = int(input())
for _ in range(T):
    a, b, n = map(int, input().split())
    if a == b:
        print(0)
    elif ((a > 0 and b > 0) or (n % 2 == 1)) and a > b:
        print(1)
    else:
        print(2)