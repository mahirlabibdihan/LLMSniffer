t = int(input())
def snek(a):
    c = 0
    while a > 1:
        a //= 2
        c += 1
    return c

for i in range(t):
    n, k = list(map(int, input().split()))
    if n == 1:
        print(k)
    elif n == 2:
        if k == 1:
            print(1, 1)
        elif k == 2:
            print(2, 1)
        else:
            print(2 ** snek(k), 2 ** snek(k) - 1)
    else:
        if k == 1:
            for j in range(n):
                print(1, end = " ")
            print()
        elif k == 2:
            print(2, end = " ")
            for j in range(n - 1):
                print(1, end = " ")
            print()
        elif k == 3:
            if n % 2 == 0:
                print(2, 1, end = " ")
                for j in range(n - 2):
                    print(1, end = " ")
                print()
            else:
                print(3, end = " ")
                for j in range(n - 1):
                    print(1, end = " ")
                print()
        else:
            if n % 2 == 0:
                print(2 ** snek(k), 2 ** snek(k) - 1, end = " ")
                for j in range(n - 2):
                    print(1, end = " ")
                print()
            else:
                print(2 ** snek(k), 2 ** snek(k) - 2, end = " ")
                for j in range(n - 2):
                    print(1, end = " ")
                print()