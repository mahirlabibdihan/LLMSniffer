def solve():
    T = int(input())
    for _ in range(T):
        C = int(input())
        xor = 0
        for _ in range(C):
            n, m = map(int, input().split())
            xor ^= (n % 2) ^ (m % 2)
        if xor == 0:
            print("Football")
        else:
            print("MasterChef")

solve()