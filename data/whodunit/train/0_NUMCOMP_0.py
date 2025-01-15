T = int(input())
for _ in range(T):
    a, b, n = map(int, input().split())
    if a**n > b**n:
        print(1)
    elif a**n < b**n:
        print(2)
    else:
        print(0)