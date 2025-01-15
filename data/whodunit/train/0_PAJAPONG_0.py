T = int(input())
for _ in range(T):
    X, Y, K = map(int, input().split())
    if ((X + Y) // K) % 2 == 0:
        print("Chef")
    else:
        print("Paja")