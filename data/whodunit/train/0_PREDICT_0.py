T = int(input())
for _ in range(T):
    PA = float(input())
    PB = 1 - PA
    if PA > PB:
        print(10000 * (1 + (2 * PB)))
    else:
        print(10000 * (1 + (2 * PA)))