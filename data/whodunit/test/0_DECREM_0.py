T = int(input().strip())
for _ in range(T):
    L, R = map(int, input().strip().split())
    if R >= 2*L:
        print(-1)
    else:
        print(R)