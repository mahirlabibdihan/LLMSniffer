def solve():
    n = int(input())
    if (n == 1):
        return 0.45
    if (n==2):
        return 0.945
    if (n==3):
        return 1.4445
    if (n==4):
        return 1.94445
    if (n==5):
        return 2.444445
    if (n==6):
        return 2.9444445
    if (n%2 == 1):
        return n//2 + 0.444444444
    else:
        return n//2-1 + 0.944444444
for _ in range(int(input())):
    print(solve())